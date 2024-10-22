from .storage import generate_key,encrypt,decrypt


def encrypt_with_key(password):
    """generates a fernet key & encrypts the password string and returns a combined string containing them both"""
    key = generate_key()
    encrypted_password = encrypt(password, key)
    combined_string = f"{encrypted_password.decode()}:{key.decode()}"
    return combined_string


def decrypt_with_key(encrypted_string):
    """takes the encrypted string and divides them into password and key , then uses decrypt function to return decrypted password"""
    encrypted_password, key = encrypted_string.split(":")
    encrypted_password_bytes = encrypted_password.encode()
    key_bytes = key.encode()
    decrypted_password = decrypt(encrypted_password_bytes, key_bytes)
    return decrypted_password
