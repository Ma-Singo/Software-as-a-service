from django.urls import path
from .views import SignupView, profile_view, signup_view, register_view

urlpatterns = [
    #path('signup/', SignupView.as_view(), name='signup'),
    #path('signup/', signup_view, name='signup'),
    path('register/', register_view, name='signup'),
    path('profile', profile_view, name='profile')
]