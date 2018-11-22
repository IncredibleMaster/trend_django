from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework.generics import GenericAPIView

from trench.views.base import MFACodeLoginMixin, MFACredentialsLoginMixin


class ObtainAuthTokenMixin:
    def handle_user_login(self, serializer, *args, **kwargs):
        return self._action(serializer)


class AuthTokenLoginOrRequestMFACode(MFACredentialsLoginMixin,
                                     ObtainAuthTokenMixin,
                                     TokenCreateView,
                                     GenericAPIView):
    pass


class AuthTokenLoginWithMFACode(MFACodeLoginMixin,
                                ObtainAuthTokenMixin,
                                GenericAPIView):
    pass


AuthTokenLogoutView = TokenDestroyView
