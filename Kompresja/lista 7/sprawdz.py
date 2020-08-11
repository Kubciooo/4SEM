import sys
from bitarray import bitarray
from numpy import random



def check_bits(byte1, byte2, result):
    bits1 = format(byte1, '08b')
    bits2 = format(byte2, '08b')

    bits11, bits12 = bits1[:4], bits1[4:]
    bits21, bits22 = bits2[:4], bits2[4:]

    s = 0
    if bits11 != bits21: 
        s+=1 
    if bits22 != bits12:
        s+=1
    result.append(s)


if __name__ == "__main__":
    
    results = []
    with open(sys.argv[1],'rb') as f1:
        with open(sys.argv[2], 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()

            for i in range(len(content1)):
                check_bits(content1[i], content2[i], results)
        

    print(sum(results))




