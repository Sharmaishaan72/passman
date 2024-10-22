from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt(message, key):
    """encrypts the message (or a string) and returns the encrypted version"""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


def decrypt(encrypted_message, key):
    """decrypts the encrypted string (or bytes) and returns the decrypted version"""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


