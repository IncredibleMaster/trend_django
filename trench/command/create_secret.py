from pyotp import random_base32
from typing import Callable

from trench.settings import TrenchAPISettings, trench_settings


class CreateSecretCommand:
    def __init__(self, generator: Callable, settings: TrenchAPISettings):
        self._generator = generator
        self._settings = settings

    def execute(self) -> str:
        return self._generator(length=self._settings.SECRET_KEY_LENGTH)


create_secret_command = CreateSecretCommand(
    generator=random_base32, settings=trench_settings
).execute
