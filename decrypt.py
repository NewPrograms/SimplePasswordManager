import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class Decrypt:
    def __init__(self, password):
        key = 'aPe7dg6RoM9t4SmL'
        self.password = password
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
    def decrypt(self):
        self.decrypt_password = b64decode(self.password)
        iv = self.decrypt_password[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        self.password = cipher.decrypt(self.decrypt_password[self.block_size:]).decode("utf-8")
        return self.__unpad(self.password)
        
    
    def __unpad(self, password):
        last_character = self.password[len(password) - 1:]
        bytes_to_remove = ord(last_character)
        return self.password[:-bytes_to_remove]