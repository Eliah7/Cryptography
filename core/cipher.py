"""
An interface representing a cryptographic scheme aka cipher
"""

class Cipher(object):
    def __init__(self):
        object.__init__(self)

    def encrypt(self, plain_text):
        raise NotImplementedError

    def decrypt(self, cipher_text):
        raise NotImplementedError

