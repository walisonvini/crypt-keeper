from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.CRYPTOGRAPHY_KEY)

def encrypt(text: str) -> bytes:
    encoded_text = text.encode()
    encrypted_text = fernet.encrypt(encoded_text)

    return encrypted_text.decode("utf-8")

def decrypt(encrypted_text: bytes) -> str:
    decoded_text = encrypted_text.encode("utf-8")
    decrypted_text = fernet.decrypt(decoded_text)

    return decrypted_text.decode()