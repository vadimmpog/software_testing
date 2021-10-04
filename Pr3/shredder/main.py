import os

PATH = os.path.dirname(__file__)
FILE_NAME = 'testfile.txt'
FILE_PATH = os.path.join(PATH, FILE_NAME)
FILE_DATA = 'Credentials\n' \
            'Email: somemail@gmail.com\n' \
            'Password: secret\n' \
            'Bank card: 13214564797\n' \
            'CVV: 456'


class TestCreator:

    def test_create_file(self):
        file = open(FILE_NAME, 'w')
        file.close()
        assert os.path.isfile(FILE_PATH)

    def test_fill_file(self):
        file = open(FILE_NAME, 'w+')
        file.write(FILE_DATA)
        file.close()
        file = open(FILE_NAME, 'r')
        assert file.read() == FILE_DATA


class TestShredder:

    def test_delete_file(self):
        os.remove(FILE_PATH)
        assert not os.path.isfile(FILE_PATH)

    def test_cipher_file(self):
        # os.
        'cipher /w:driveletter:\foldername'
        assert None


class TestInspector:

    def test_check_file(self):
        assert None
