from django.urls import path
from .views import SignupView, profile_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile', profile_view, name='profile')
]