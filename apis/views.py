from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from users.models import CustomUser
from customers.models import Customer
from apis.serializers import UserSerializer, CustomerSerializer


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


class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        data = CustomerSerializer(customers, many=True).data
        return Response(data)

class CustomerDetail(APIView):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        data = CustomerSerializer(customer).data
        return Response(data)
    

class UserSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    
class CustomerSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer