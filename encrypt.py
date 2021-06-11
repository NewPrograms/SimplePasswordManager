import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
class Encryption:

    def __init__(self):
        key = 'aPe7dg6RoM9t4SmL'
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        
    def __pad(self, password):
        number_of_bytes_to_pad = self.block_size - len(password) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        self.padded_password = password + padding_str
        return self.padded_password

    def encrypt(self, password):
        self.password = self.__pad(password)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        self.encrypted_password = cipher.encrypt(self.password.encode())
        return b64encode(iv + self.encrypted_password).decode("utf-8")
        


