from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()

def encrypt_message(message):
    key: str = "rfeL8nyqa98KaPnB9BYdTuH5A-acVOILRi1ZNeSywdE=" 
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key: str = "rfeL8nyqa98KaPnB9BYdTuH5A-acVOILRi1ZNeSywdE=" 
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


