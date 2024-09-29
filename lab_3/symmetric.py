import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from work_with_files import *


def generation_key(size_key: int) -> bytes:

    if size_key not in [128, 192, 256]:
        raise ValueError("Invalid key length. Please choose 128, 192, or 256 bits.")
    key = os.urandom(size_key)
    return key


def key_serialization(key: bytes, path: str) -> None:

    try:
        with open(path, 'wb') as key_file:
            key_file.write(key)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def key_deserialization(path: str) -> bytes:

    try:
        with open(path, "rb") as file:
            key = file.read()
        return key
    
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")





