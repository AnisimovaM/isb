from work_with_files import *

def create_substitution_cipher(key_path: str, alphabet_path: str) -> dict:

    alphabet = read_json_from_file(alphabet_path)
    alphabet = alphabet["russian_alphabet"]

    key = read_json_from_file(key_path)
    key = key["key"]

    cipher_dict = {alphabet[i]: key[i] for i in range(len(alphabet))}
    return cipher_dict


def encrypt(text: str, cipher_dict: dict) -> str:
    
    encrypted_text = ""
    for char in text:
        if char.upper() in cipher_dict:
            encrypted_char = cipher_dict[char.upper()]
            if char.islower():
                encrypted_text += encrypted_char.lower()
            else:
                encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def task1() -> None:

    settings = read_json_from_file("settings.json")

    cipher_dict = create_substitution_cipher(settings["key_file_path"], settings["alphabet_path"])

    input_text = read_text_from_file(settings["input_file_task1_path"])
    encrypted_text = encrypt(input_text, cipher_dict)

    write_text_to_file(settings["output_file_task1_path"], encrypted_text)
    
    