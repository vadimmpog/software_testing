import os
import random
import sys


class Creator:

    def __init__(self, file_name, file_data, path) -> None:
        self.path = os.path.dirname(__file__)
        self.file_name = file_name
        self.file_path = os.path.join(path, file_name)
        self.file_data = file_data

    def create_file(self):
        file = open(self.file_name, 'w')
        file.close()

    def fill_file(self):
        file = open(self.file_name, 'w+')
        file.write(self.file_data * 10)
        file.close()


class ShredderWindows:

    def __init__(self, file_name, path) -> None:
        self.path = path
        self.file_name = file_name
        self.file_path = os.path.join(path, file_name)

    def overwrite_file(self):
        file = open(self.file_path, 'w+')
        for _ in range(0, random.randint(0, 150)):
            file.write(chr(random.randint(95, 120)) + " ")
        file.close()

    def delete_file(self):
        os.remove(self.file_path)

    def cipher_file(self):
        return os.system(f'cipher /w:{self.path}') == 0


class ShredderLinux:

    def __init__(self, file_name, path) -> None:
        self.path = path
        self.file_name = file_name
        self.file_path = os.path.join(path, file_name)

    def shred_file(self):
        return os.system(f'shred -u {self.file_path}') == 0


if __name__ == '__main__':
    path = os.path.dirname(__file__)
    file_name = 'testfile'
    file_data = 'Credentials\n' \
                'Email: somemail@gmail.com\n' \
                'Password: secret\n' \
                'Bank card: 13214564797\n' \
                'CVV: 456\n' \
                'Other important private information\n'
    creator = Creator(file_name, file_data, path)
    creator.create_file()
    creator.fill_file()
    if sys.platform.startswith("win"):
        shredder = ShredderWindows(file_name, path)
        shredder.overwrite_file()
        method = input('On windows you can choose method v1 or v2:\n')
        if method == 'v1':
            shredder.delete_file()
        elif method == 'v2':
            shredder.cipher_file()
        else:
            print('Wrong method')
    else:
        shredder = ShredderLinux(file_name, path)
        shredder.shred_file()
