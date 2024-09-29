import math
import mpmath

from work_with_files import *

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


def nist_frequency_bit_test(bit_sequence: str, file_path: str, key: str) -> None:

    try:
        sequence_else = [1 if bit == "1" else -1 for bit in bit_sequence]
        s_n = sum(sequence_else) / math.sqrt(len(sequence_else))
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_text_to_file(file_path, f'{key} : {p_v}\n')
    except ZeroDivisionError:
        print("Frequency bit test. Error: Division by zero")
    except Exception as e:
        print("Frequency bit test. Error: ", e)



