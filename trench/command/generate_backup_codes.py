from django.utils.crypto import get_random_string

from typing import Callable, Set

from trench.settings import trench_settings


class GenerateBackupCodesCommand:
    def __init__(self, random_string_generator: Callable):
        self._random_string_generator = random_string_generator

    def execute(
        self,
        quantity: int = trench_settings.BACKUP_CODES_QUANTITY,
        length: int = trench_settings.BACKUP_CODES_LENGTH,
        allowed_chars: str = trench_settings.BACKUP_CODES_CHARACTERS,
    ) -> Set[str]:
        """
        Generates random encrypted backup codes.

        :param quantity: How many codes should be generated
        :type quantity: int
        :param length: How long codes should be
        :type length: int
        :param allowed_chars: Characters to create backup codes from
        :type allowed_chars: str

        :returns: Encrypted backup codes
        :rtype: set[str]
        """
        return {
            self._random_string_generator(length, allowed_chars)
            for _ in range(quantity)
        }


generate_backup_codes_command = GenerateBackupCodesCommand(
    random_string_generator=get_random_string,
).execute
