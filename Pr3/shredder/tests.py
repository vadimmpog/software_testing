import os
import sys
import main
import pytest

path = os.path.dirname(__file__)
file_name = 'testfile'
file_data = 'Credentials\n' \
            'Email: somemail@gmail.com\n' \
            'Password: secret\n' \
            'Bank card: 13214564797\n' \
            'CVV: 456\n' \
            'Other important private information\n'


class TestCreator:
    test_creator = main.Creator(file_name, file_data, path)

    def test_create_file(self):
        self.test_creator.create_file()
        assert os.path.isfile(file_name)

    def test_fill_file(self):
        self.test_creator.fill_file()
        file = open(file_name, 'r')
        assert file.read() == file_data * 10


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="not Windows")
class TestShredderWindows:
    shredder = main.ShredderWindows(file_name, path)

    def test_overwrite_file(self):
        self.shredder.overwrite_file()
        file = open(self.shredder.file_path)
        assert not file.read() == file_data * 10

    def test_delete_file(self):
        self.shredder.delete_file()
        assert not os.path.isfile(self.shredder.file_path)

    @pytest.mark.skip
    def test_cipher_file(self):
        assert os.system(f'cipher /w:{path}') == 0


@pytest.mark.skipif(sys.platform.startswith("win"), reason="not Linux")
class TestShredderLinux:
    shredder = main.ShredderLinux(file_name, path)

    def test_shred_file(self):
        assert self.shredder.shred_file()