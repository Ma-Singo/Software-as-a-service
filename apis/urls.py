from django.urls import path
from rest_framework.routers import DefaultRouter

from apis.views import (
    UserDetail, UserList,
    CustomerList, CustomerDetail,
    CustomerSet,
    UserSet,
)

router = DefaultRouter()
router.register('customers', CustomerSet, basename='customer_list')
router.register('users', UserSet, basename='user_list')


urlpatterns = [

    path('user/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('customer/<int:pk>/', CustomerDetail.as_view(), name="customer_detail"),
]

urlpatterns += router.urls