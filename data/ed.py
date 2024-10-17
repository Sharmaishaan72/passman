from .storage import generate_key,encrypt,decrypt


def encrypt_with_key(password):
    key = generate_key()
    encrypted_password = encrypt(password, key)
    combined_string = f"{encrypted_password.decode()}:{key.decode()}"
    return combined_string


def decrypt_with_key(encrypted_string):
    encrypted_password, key = encrypted_string.split(":")
    encrypted_password_bytes = encrypted_password.encode()
    key_bytes = key.encode()
    decrypted_password = decrypt(encrypted_password_bytes, key_bytes)
    return decrypted_password
