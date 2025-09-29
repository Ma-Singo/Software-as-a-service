from django.urls import path

from users.views import SignupView, profile_view, signup_view, register_view
from users.apiviews import UserList, UserDetail

urlpatterns = [
    #path('signup/', SignupView.as_view(), name='signup'),


    path('signup/', register_view, name='signup'),
    path('profile', profile_view, name='profile'),

    # API 
    path('', UserList.as_view(), name="user_list"),
    path('user/<int:pk>/', UserDetail.as_view(), name="user_detail"),
]