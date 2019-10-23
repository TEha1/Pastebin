from django.urls import path, include
# from .views import UserCL, UserRUD, FollowCL, FollowRUD, UploadCL, UploadRUD
from rest_framework import routers

from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view())

]
