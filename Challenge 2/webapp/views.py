from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import users
from . serializers import userSerializer

def jwt_response_payload_handler(token, user=None, request=None):

    return {
        "status" : "success" , "message" : "user_authed"
    }

class userList(APIView):

    def get(self, request):
        user = users.objects.all()
        serializer = userSerializer(user, many=True)
        return Response(serializer.data)


    def post(self, request):
        pass
# Create your views here.
