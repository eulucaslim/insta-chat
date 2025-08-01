from setup.settings import USERNAME, PASSWORD
from instagrapi import Client

class Instagram(object):

    def __init__(self):
        self.client = Client()
        self.username = USERNAME
        self.password = PASSWORD
        self.user_id = None
    
    def login(self) -> bool:
        try:
            self.client.login(self.username, self.password)
            self.user_id = self.client.user_id
            return True
        except Exception as e:
            raise (e)

    def get_all_followers(self) -> dict:
        all_followers = self.client.user_followers_v1(self.user_id)
        usernames = [follower.username for follower in all_followers.values()]
        return usernames
