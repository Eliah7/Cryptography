from unittest import TestCase
from subsititution_encryption.ceasar.ceasar_cipher import CeasarCipher

class TestCeasarCipher(TestCase):
    """
    Test case suit for the Ceasar Cipher
    Methods:
        => encrypt()
        => decrypt()
    Testing Dimensions:
        => shift size
        => alphabet change
        => case sensitivity
        => space in alphabet
    """

    def tearDown(self):
        self.cipher = None
        self.plain_text = None
        self.cipher_text = None

    def test_encrypt_shift_3_alphabet_ascii_no_case_no_space(self):
        self.cipher = CeasarCipher(shift=3)
        self.plain_text = "thisisaname"
        self.cipher_text = "wklvlvdqdph"
        self.assertEqual(self.cipher.encrypt(plain_text=self.plain_text), self.cipher_text)

    def test_decrypt_shift_3_alphabet_ascii_no_case_no_space(self):
        self.cipher = CeasarCipher(shift=3)
        self.plain_text = "theobserveristheobserved"
        self.cipher_text = "wkhrevhuyhulvwkhrevhuyhg"
        self.assertEqual(self.cipher.decrypt(cipher_text=self.cipher_text), self.plain_text)

    def test_encrypt_shift_7_alphabet_ascii_no_case_no_space(self):
        self.cipher = CeasarCipher(shift=7)
        self.plain_text = "thisisaname"
        self.cipher_text = "aopzpzhuhtl"
        self.assertEqual(self.cipher.encrypt(plain_text=self.plain_text), self.cipher_text)

    def test_decrypt_shift_7_alphabet_ascii_no_case_no_space(self):
        self.cipher = CeasarCipher(shift=7)
        self.plain_text = "theobserveristheobserved"
        self.cipher_text = "aolvizlyclypzaolvizlyclk"
        self.assertEqual(self.cipher.decrypt(cipher_text=self.cipher_text), self.plain_text)

    def test_encrypt_shift_3_alphabet_ascii_no_case_with_space(self):
        self.cipher = CeasarCipher(shift=3)
        self.plain_text = "this is a name"
        self.cipher_text = "wklv lv d qdph"
        self.assertEqual(self.cipher.encrypt(plain_text=self.plain_text), self.cipher_text)

    def test_decrypt_shift_3_alphabet_ascii_no_case_with_space(self):
        self.cipher = CeasarCipher(shift=3)
        self.plain_text = "the observer is the observed"
        self.cipher_text = "wkh revhuyhu lv wkh revhuyhg"
        self.assertEqual(self.cipher.decrypt(cipher_text=self.cipher_text), self.plain_text)

    def test_encrypt_shift_7_alphabet_ascii_no_case_with_space(self):
        self.cipher = CeasarCipher(shift=7)
        self.plain_text = "this is a name"
        self.cipher_text = "aopz pz h uhtl"
        self.assertEqual(self.cipher.encrypt(plain_text=self.plain_text), self.cipher_text)

    def test_decrypt_shift_7_alphabet_ascii_no_case_with_space(self):
        self.cipher = CeasarCipher(shift=7)
        self.plain_text = "the observer is the observed"
        self.cipher_text = "aol vizlycly pz aol vizlyclk"
        self.assertEqual(self.cipher.decrypt(cipher_text=self.cipher_text), self.plain_text)

    def test_encrypt_shift_3_alphabet_ascii_case_sensitive_with_space(self):
        self.cipher = CeasarCipher(shift=3, is_case_sensitive=True)
        self.plain_text = "This is a name"
        self.cipher_text = "Tklv lv d qdph"
        self.assertEqual(self.cipher.encrypt(plain_text=self.plain_text), self.cipher_text)

    def test_decrypt_shift_3_alphabet_ascii_case_sensitive_with_space(self):
        self.cipher = CeasarCipher(shift=3, is_case_sensitive=True)
        self.plain_text = "The observer is the observed"
        self.cipher_text = ""
        self.assertEqual(self.cipher.decrypt(cipher_text=self.cipher_text), self.plain_text)

    def test_encrypt_shift_7_alphabet_ascii_case_sensitive_with_space(self):
        self.cipher = CeasarCipher(shift=7, is_case_sensitive=True)
        self.plain_text = "This is a name"
        self.cipher_text = "Topz pz h uhtl"
        self.assertEqual(self.cipher.encrypt(plain_text=self.plain_text), self.cipher_text)

    def test_decrypt_shift_7_alphabet_ascii_case_sensitive_with_space(self):
        self.cipher = CeasarCipher(shift=7, is_case_sensitive=True)
        self.plain_text = "The observer is the observed"
        self.cipher_text = "Tol vizlycly pz aol vizlyclk"
        self.assertEqual(self.cipher.decrypt(cipher_text=self.cipher_text), self.plain_text)


