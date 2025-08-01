from core.models import ChatUser, Follower
from core.utils import Instagram, save_instance, get_instance
from core.serializers import LoginInstaSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from setup.settings import logger
# Create your views here
class GetAllFollowersViewSet(viewsets.ViewSet):

    def list(self, request):
        if request.method == "GET":
            try:
                username = request.query_params.get('username', None)
                user = ChatUser.objects.filter(username=username).first()
                insta = get_instance(user.username)
                if insta:
                    all_followers = insta.get_all_followers()
                    return Response(all_followers, status=200)
                else:
                    raise Exception("Cache is empty, Login Again Please!")
            except Exception as error:
                return Response(
                    data={"msg": str(error)},
                    status=status.HTTP_400_BAD_REQUEST
                )
class LoginInstaViewSet(viewsets.ViewSet):
    serrializer_class = LoginInstaSerializer

    def create(self, request):
        if request.method == "POST":
            try:
                username = request.data.get('username', None)
                password = request.data.get('password', None)
                instance = get_instance(username)
                if not instance:
                    if username and password:
                        insta = Instagram(username, password)
                        if insta.login():
                            save_instance(username, insta)
                            user, created = ChatUser.objects.get_or_create(
                                username=username, 
                                insta_id=insta.user_id
                            )
                            if created:
                                logger.info('User create in database!')
                            else:
                                logger.info('User already exists in database!')
                            return Response(
                                data={"msg": "Login sucessful!", "username": user.username}, 
                                status=status.HTTP_200_OK
                            )
                        else:
                            raise Exception("Error to login in Instagram, Verify your credentials")
                    else:
                        raise Exception("Send your username and password to acess!")
                else:
                    return Response(
                                data={"msg": "Login sucessful!", "username": instance.username}, 
                                status=status.HTTP_200_OK
                            )
            except Exception as error:
                return Response(
                    data={"msg": str(error)},
                    status=status.HTTP_400_BAD_REQUEST
                )