from django.conf.urls import url

from trench import views


__all__ = [
    'urlpatterns',
]

urlpatterns = [
    url(
        r'^(?P<method>[-\w]+)/activate/$',
        views.RequestMFAMethodActivationView.as_view(),
        name='mfa-activate',
    ),
    url(
        r'^(?P<method>[-\w]+)/activate/confirm/$',
        views.RequestMFAMethodActivationConfirmView.as_view(),
        name='mfa-activate-confirm',
    ),
    url(
        r'^(?P<method>[-\w]+)/deactivate/$',
        views.RequestMFAMethodDeactivationView.as_view(),
        name='mfa-deactivate',
    ),
    url(
        r'^(?P<method>[-\w]+)/codes/regenerate/$',
        views.RequestMFAMethodBackupCodesRegenerationView.as_view(),
        name='mfa-regenerate-codes',
    ),
    url(
        r'^code/request/$',
        views.RequestMFAMethodCode.as_view(),
        name='mfa-request-code',
    ),
    url(
        r'^mfa/config/$',
        views.GetMFAConfig.as_view(),
        name='mfa-config-info',
    ),
    url(
        r'^mfa/user-active-methods/$',
        views.ListUserActiveMFAMethods.as_view(),
        name='mfa-list-user-active-methods',
    ),
     url(
        r'^mfa/change-primary-method/$',
        views.ChangePrimaryMethod.as_view(),
        name='mfa-change-primary-method',
    ),
]
