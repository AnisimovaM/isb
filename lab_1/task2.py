from work_with_files import *
from collections import Counter


def analyze_character_frequency(text: str, file_path: str) -> None:

    char_count = Counter(text)
    total_chars = sum(char_count.values())
    normalized_freq = {char: count / total_chars for char, count in char_count.items()}
    write_json_to_file(file_path, normalized_freq)

    return None


def create_decryption_key(file_path: str, char_freq_dict: dict, russian_alphabet_freq: dict) -> None:

    decryption_key = {}
    used_chars = set()

    for char in sorted(char_freq_dict, key=char_freq_dict.get, reverse=True):
        closest_match = max(russian_alphabet_freq,
                            key=lambda x: russian_alphabet_freq[x] if x not in used_chars else -1)
        decryption_key[char] = closest_match
        used_chars.add(closest_match)

    write_json_to_file(file_path, decryption_key)


def decrypt(file_path: str, encrypted_text: str, decryption_dict: dict) -> None:

    decrypted_text = ''

    for char in encrypted_text:
        if char in decryption_dict:
            decrypted_text += decryption_dict[char]
        else:
            decrypted_text += char

    write_text_to_file(file_path, decrypted_text)


def task2() -> None:
    settings = read_json_from_file("settings.json")

    encrypted_text = read_text_from_file(settings["input_file_task2_path"])
    analyze_character_frequency(encrypted_text, settings["frequency_indexes_of_task2_text_path"])

    char_freq_dict = read_json_from_file(settings["frequency_indexes_of_task2_text_path"])
    russian_alphabet_freq = read_json_from_file(settings["frequency_indexes_of_russian_path"])

    create_decryption_key(settings["decryption_key_task2_path"], char_freq_dict, russian_alphabet_freq)
    decryption_dict = read_json_from_file(settings["decryption_key_task2_path"])

    decrypt(settings["output_file_task2_path"], encrypted_text, decryption_dict)
