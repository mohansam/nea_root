from cryptography.fernet import Fernet
import base64
from nea_site.settings import ENCRYPT_KEY

# source https://stackoverflow.com/questions/5131227/custom-python-encryption-algorithm
def encrypt_data(value):
    encrypted = []
    for i, c in enumerate(value):
        key_c = ord(ENCRYPT_KEY[i % len(value)])
        msg_c = ord(c)
        encrypted.append(chr((msg_c + key_c) % 127))
    return ''.join(encrypted)


def decrypt_data(encrypted_value):
    msg = []
    for i, c in enumerate(encrypted_value):
        key_c = ord(ENCRYPT_KEY[i % len(ENCRYPT_KEY)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)