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


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="not Windows")
class TestShredderWindows:

    def test_overwrite_file(self):
        file = open(FILE_NAME, 'w+')
        for _ in range(0, random.randint(0, 150)):
            file.write(chr(random.randint(0, 128)) + " ")
        assert not file.read() == FILE_DATA * 10

    def test_delete_file(self):
        os.remove(FILE_PATH)
        assert not os.path.isfile(FILE_PATH)

    @pytest.mark.skip
    def test_cipher_file(self):
        assert os.system(f'cipher /w:{PATH}') == 0


@pytest.mark.skipif(sys.platform.startswith("win"), reason="not Linux")
class TestShredderLinux:

    def test_shred_file(self):
        assert os.system(f'shred -u {FILE_PATH}') == 0
