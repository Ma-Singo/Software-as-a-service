from django.urls import path

from users.views import SignupView, profile_view, signup_view, register_view

urlpatterns = [
    #path('signup/', SignupView.as_view(), name='signup'),


    path('signup/', register_view, name='signup'),
    path('profile', profile_view, name='profile'),

]