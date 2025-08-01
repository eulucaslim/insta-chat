from django.core.cache import cache
from instagrapi import Client

class Instagram(object):

    def __init__(self, username: str, password: str):
        self.client = Client()
        self.username = username
        self.password = password
        self.user_id = None
    
    def login(self) -> bool:
        try:
            self.client.login(self.username, self.password)
            self.user_id = self.client.user_id
            return True
        except Exception as e:
            raise (e)

    def get_all_followers(self) -> list:
        all_followers = self.client.user_followers_v1(self.user_id)
        # usernames = [follower.username for follower in all_followers.values()]
        data = [
            {
                "username": user.username,
                "user_id": user.pk
            }
        for user in all_followers ]

        return data

def save_instance(username: str, insta: Instagram) -> None:
    cache.set(f"{username}", insta, timeout=3600)

def get_instance(username: str):
    instance = cache.get(f"{username}")
    if instance:
        return instance
    else:
        return False