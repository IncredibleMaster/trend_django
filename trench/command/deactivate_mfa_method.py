from django.db.transaction import atomic

from typing import Type

from trench.exceptions import DeactivationOfPrimaryMFAMethodError, MFANotEnabledError
from trench.models import MFAMethod
from trench.utils import get_mfa_model


class DeactivateMFAMethodCommand:
    def __init__(self, mfa_model: Type[MFAMethod]) -> None:
        self._mfa_model = mfa_model

    @atomic
    def execute(self, mfa_method_name: str, user_id: int) -> None:
        mfa = self._mfa_model.objects.get_by_name(user_id=user_id, name=mfa_method_name)
        active_mfa_methods = self._mfa_model.objects.list_active(user_id=user_id)
        if mfa.is_primary and len(active_mfa_methods) > 1:
            raise DeactivationOfPrimaryMFAMethodError()
        if not mfa.is_active:
            raise MFANotEnabledError()

        self._mfa_model.objects.filter(user_id=user_id, name=mfa_method_name).update(
            is_active=False
        )


deactivate_mfa_method_command = DeactivateMFAMethodCommand(
    mfa_model=get_mfa_model()
).execute
