from drf_spectacular.utils import extend_schema

from rest_framework.permissions import AllowAny
from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth import get_user_model
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
import os

from user.serializers import (
    UserRegisterRequestSerializer,
    UserRegisterResponseSerializer,
)

from core.exceptions.exceptions import RegisterWithGoogleTokenInvalid
from core.exceptions.exception_serializer import ExceptionSerializer


class LoginWithGoogle(KnoxLoginView):
    permission_classes = (AllowAny,)

    @extend_schema(
        request=UserRegisterRequestSerializer,
        responses={
            200: UserRegisterResponseSerializer,
            400: ExceptionSerializer, },
        description='Register new account to access the api',)
    def post(self, request, format=None):
        try:
            google_credential = request.data.get('credential')
            CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID'),
            user_info = id_token.verify_oauth2_token(
                google_credential, requests.Request(), CLIENT_ID
            )
            email = user_info['email']
            name = user_info['name']
        except ValueError:
            raise RegisterWithGoogleTokenInvalid()

        user, is_new_user = get_user_model().objects.get_or_create(
            email=email, name=name
        )
        if not is_new_user:
            user.auth_token_set.all().delete()

        login(request, user)
        return super(LoginWithGoogle, self).post(request, format=None)

    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data
