# django
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
# rest_framework
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# serializer
from .serializers import UserSerializer


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Hash User Password
        posted_data = serializer.validated_data
        hashed_password = make_password(posted_data['password'])
        posted_data['password'] = hashed_password
        return serializer.save()


class UserLoginView(APIView):

    def post(self, *args, **kwargs):
        posted_data = self.request.data

        try:
            username = posted_data['username']
        except MultiValueDictKeyError:
            return Response({
                "Error": "Empty username"
            })

        try:
            password = posted_data['password']
        except MultiValueDictKeyError:
            return Response({
                "Error": "Empty password"
            })

        try:
            user = User.objects.get(username = username)
        except ObjectDoesNotExist:
            return Response({
                "Error": "This user not found"
            })

        if check_password(password=password, encoded=user.password):
            user_json = UserSerializer(user)
            try:
                token =  Token.objects.get(user=user)
                return Response({
                    "token": token.key,
                    "user": user_json.data
                })
            except ObjectDoesNotExist:
                return Response({
                    "token": "",
                    "user": user_json.data
                })

        return Response({
            "Error": "incorrect password"
        })
