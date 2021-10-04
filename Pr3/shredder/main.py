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

    @pytest.mark.V1
    def test_overwrite_file(self):
        file = open(FILE_NAME, 'w+')
        for _ in range(0, random.randint(0, 150)):
            file.write(str(random.randint(0, 128)) + " ")

    @pytest.mark.V1
    def test_rename_file(self):
        new_name = ''
        for i in range(0, random.randint(0, 20)):
            new_name += chr(i * 6)
        os.rename(FILE_NAME, new_name)

    @pytest.mark.V1
    @pytest.mark.V2
    def test_delete_file(self):
        os.remove(FILE_PATH)
        assert not os.path.isfile(FILE_PATH)

    @pytest.mark.V2
    def test_cipher_file(self):
        assert os.system(f'cipher /w:{PATH}') == 0


@pytest.mark.Linux
class TestShredderLinux:

    def test_shred_file(self):
        assert os.system(f'shred -u {FILE_PATH}') == 0
