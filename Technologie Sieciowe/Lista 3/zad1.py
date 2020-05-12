import zlib
from random import choice

"Konfiguracja wstępna"
FLAG = "0111110"
STUFFING_MAX_COUNT = FLAG.count('1')
CRC_SIZE = 32

def crc_check(s):
    crc = "{0:b}".format(zlib.crc32(s.encode()))
    deficit = 32 - len(crc)
    return '0' * deficit + crc

def bit_stuffing(s):
    result = ''
    ones_count = 0
    for c in s:
        result += c
        if c == '1':
            ones_count += 1
            if ones_count == STUFFING_MAX_COUNT: 
                result += '0'
                ones_count = 0
        else:
            ones_count = 0
    return result

def reverse_bit_stuffing(s):
    result = ''
    ones_count = 0
    for c in s:
        if c == '1':
            ones_count += 1
            result += c
        else:
            if ones_count < STUFFING_MAX_COUNT:
                result += c
            ones_count = 0            
    return result



"Tworzenie ramek "
def encode_frame(s):
    return FLAG + bit_stuffing(s+crc_check(s)) + FLAG

def decode_frame(s):
    decoded = reverse_bit_stuffing(s[len(FLAG):(-len(FLAG))])
    data = decoded[:len(decoded) - CRC_SIZE]
    crc = decoded[len(decoded) - CRC_SIZE:]
    if (crc_check(data) == crc):
        return data
    else:
        return ""

"Funkcje testujące"
def create_bitlist(size = 1000):
    return ''.join(choice('01') for _ in range(size))


def create_test_file(input = "input.txt"):
    with open(input, "w") as f:
        f.write(create_bitlist())

"Wczytywanie i zapisywanie do plików "
def encode_file(input = "input.txt", output = "encoded_input.txt"):
    with open(input, 'r') as f:
        content = f.read()
    with open(output, 'w') as f:
        f.write(encode_frame(content))


def decode_file(input = "encoded_input.txt", output = "decoded_input.txt"):
    with open(input, 'r') as f:
        content = f.read()
    with open(output, 'w') as f:
        f.write(decode_frame(content))

    

def main():
    create_test_file()
    encode_file()
    decode_file()
    print(bit_stuffing("11010111111001011111101010111111011"))
if __name__ == "__main__":
    main()