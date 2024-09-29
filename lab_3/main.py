import argparse
from work_with_files import *
import symmetric
import assymetric

def menu():

    parser = argparse.ArgumentParser()
    settings = read_json_from_file("settings.json")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Generate symmetric and asymmetric keys')
    group.add_argument('-enc', '--encryption', help='Encrypt a file using symmetric key')
    group.add_argument('-dec', '--decryption', help='Decrypt a file using symmetric key')
    group.add_argument('-enc_sym', '--encryption_symmetric', help='Encrypt sym key using asym encryption')
    group.add_argument('-dec_sym', '--decryption_symmetric', help='Decrypt sym key using asym decryption')


    args = parser.parse_args()

    match args:
        case args if args.generation:
            key_length = int(input(
                    "Enter the key length in bits, in the range [128, 192, 256]: "
                ))
            print(f"Your key length: {key_length} ")

            symmetric.generation_key(key_length)

        case args if args.encryption:
            pass
        case args if args.decryption:
            pass
        case args if args.encryption_symmetric:
            pass
        case args if args.decryption_symmetric:
            pass


if __name__ == "__main__":
    menu()