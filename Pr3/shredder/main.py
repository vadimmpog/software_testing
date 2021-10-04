import os
import random
import sys

import pytest

PATH = os.path.dirname(__file__)
FILE_NAME = 'testfile'
FILE_PATH = os.path.join(PATH, FILE_NAME)
FILE_DATA = 'Credentials\n' \
            'Email: somemail@gmail.com\n' \
            'Password: secret\n' \
            'Bank card: 13214564797\n' \
            'CVV: 456\n' \
            'Other important private information\n'

IS_WIN = sys.platform.startswith('win')


class TestCreator:

    def test_create_file(self):
        file = open(FILE_NAME, 'w')
        file.close()
        assert os.path.isfile(FILE_PATH)

    def test_fill_file(self):
        file = open(FILE_NAME, 'w+')
        file.write(FILE_DATA * 10)
        file.close()
        file = open(FILE_NAME, 'r')
        assert file.read() == FILE_DATA * 10


@pytest.mark.Win
class TestShredderWindows:

    def test_overwrite_file(self):
        file = open(FILE_NAME, 'w+')
        for _ in range(0, random.randint(0, 1) * 50):
            file.write(str(random.randint(0, 1)) + " ")

    def test_delete_file(self):
        os.remove(FILE_PATH)
        assert not os.path.isfile(FILE_PATH)

    @pytest.mark.V2
    def test_cipher_file(self):
        if IS_WIN:
            os.system(f'cipher /w:{PATH}')
        assert None


@pytest.mark.Linux
class TestShredderLinux:

    def test_shred_file(self):
        os.system(f'shred -u {FILE_PATH}')
        assert None
