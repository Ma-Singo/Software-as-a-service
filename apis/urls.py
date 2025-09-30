from django.urls import path

from apis.views import (
    UserDetail,
    UserList,
    CustomerList,
    CustomerDetail
)

urlpatterns = [
    path('users/', UserList.as_view(), name="user_list"),
    path('user/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetail.as_view(), name="customer_detail"),
]