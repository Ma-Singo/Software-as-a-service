from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializer import UserSerializer

class UserList(APIView):
    def get(self, request):
        users = CustomUser.objects.get()
        data = UserSerializer(users, many=True).data
        return Response(data)


class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        data = UserSerializer(user).data
        return Response(data)