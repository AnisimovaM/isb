from work_with_files import *
from collections import Counter


def analyze_character_frequency(text: str, file_path: str) -> None:

    char_count = Counter(text)
    total_chars = sum(char_count.values())
    normalized_freq = {char: count / total_chars for char, count in char_count.items()}
    write_json_to_file(file_path, normalized_freq)


def create_decryption_key(file_path: str, char_freq_dict: dict, russian_alphabet_freq: dict) -> None:

    decryption_key = {}
    used_chars = set()

    sorted_encrypted_chars = sorted(char_freq_dict, key=char_freq_dict.get, reverse=True)

    for char in sorted_encrypted_chars:

        closest_match = None
        max_frequency = -1

        for russian_char in russian_alphabet_freq:
            if russian_char not in used_chars and russian_alphabet_freq[russian_char] > max_frequency:
                closest_match = russian_char
                max_frequency = russian_alphabet_freq[russian_char]

        if closest_match:
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
    decryption_key = read_json_from_file(settings["decryption_key_task2_path"])

    decrypt(settings["output_file_task2_path"], encrypted_text, decryption_key)
