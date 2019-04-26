"""
Caesar Cipher Technique is the simple and easy method of encryption technique.

It is simple type of substitution cipher.

Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.
"""
from core.cipher import Cipher
from string import *
from utils.string_array_operations import *

class CeasarCipher(Cipher):
    def __init__(self, alphabet=ascii_lowercase, shift=3, is_case_sensitive=False):
        Cipher.__init__(self)
        self.alphabet_array = stringToArray(alphabet)
        self.shift = shift
        self.is_case_sensitive = is_case_sensitive

    def encrypt(self, plain_text):
        return self.encrypt_decorator_function(plain_text)

    def decrypt(self, cipher_text):
        return self.decrypt_decorator_function(cipher_text)

    def text_transformer(operator_function):
        """
        Is a decorator function that converts
                cipher_text => cipher_text_array => mathematical operation => plain_text_array => plain_text and
                plain_text => plain_text_array => mathematical operation =>cipher_text_array => cipher_text

        The only difference between encrypt and decrypt is
                encrypt uses + as the mathematical operation
                decrypt uses - as the mathematical operation
        """
        def wrapper(self, text):
            # TODO: sanitization of inputs at every stage
            resulting_text_array = []
            text_lower_array = stringToArray(text.lower())

            for letter in text_lower_array:
                if letter == " ":
                    resulting_text_array.append(" ") # dealing with spaces which are not in the alphabet
                else:
                    letter_index = self.alphabet_array.index(letter)
                    resulting_text_array.append(self.alphabet_array[(operator_function(self, letter_index,self.shift)) % len(self.alphabet_array)])

            resulting_text = arrayToString(resulting_text_array)
            return resulting_text
        return wrapper

    @text_transformer
    def decrypt_decorator_function(self, letter_index, shift):
        return letter_index - shift

    @text_transformer
    def encrypt_decorator_function(self, letter_index, shift):
        return letter_index + shift
