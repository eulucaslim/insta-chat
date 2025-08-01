from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()

router.register('get_all_followers', views.GetAllFollowersViewSet,
                basename='get_all_followers')

urlpatterns = [
    path('', include(router.urls))
]