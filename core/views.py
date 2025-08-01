from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class GetAllFollowersViewSet(viewsets.ViewSet):

    def create(self, request):
        if request.method == "POST":
            return Response({"Hello": "World"})
