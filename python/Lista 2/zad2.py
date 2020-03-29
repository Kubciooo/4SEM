import sys

array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

slownik = {}
for i in range(len(array)):
    s = "{0:06b}".format((i))
    slownik[array[i]] = s

def string_to_bin(s):
    result = ''
    for c in s:
        ascii_representation = ord(c)
        formatted_binary = "{0:08b}".format(ascii_representation)
        for binary in formatted_binary:
            result += binary
    return result
def bin_to_list(s):
    result = []
    for c in s:
        result.append(c)
    return result


def koduj(s):
    binary_table = bin_to_list(s)
    iterator = 0
    result = ''
    s = ''
    while iterator < len(binary_table):
        if iterator % 6 == 0 and iterator != 0: 
            result += (array[int(s,2)])
            s = ''
        s += binary_table[iterator]
        iterator += 1
    result += (array[int(s,2)])
    return result

def dekoduj(s):
    result = []
    for c in s:
        binary_representation = slownik[c]
        for b in binary_representation:
            result.append(b)
    iterator = 0
    r = ''
    r2 = ''
    pom = ''
    while iterator < len(result):
        if iterator % 8 == 0 and iterator > 0: 
            pom += str(chr(int(r,2)))
            r = ''
        r += result[iterator]
        r2 += result[iterator]
        iterator += 1
    pom += str(chr(int(r,2)))
    return r2, pom
#print(stringToBin("Python"))

#a,b = dekoduj("UHl0aG9u")
#print(b)
#print(koduj(a))
c = sys.argv

if len(c) != 4:
    print("Niepoprawny format wejściowy")
else:
    filename_read = c[2]
    filename_write = c[3] 
    file_write = open(filename_write, "w+")
    file_read = open(filename_read, "r")
    if c[1] == '--decode':
        line = file_read.read()
        a, b = dekoduj(line)
        file_write.write(a)
    elif c[1] == '--encode':
        line = file_read.read()
        a = koduj(line)
        file_write.write(a)
    else:
        print("Niepoprawny format wejściowy")

        