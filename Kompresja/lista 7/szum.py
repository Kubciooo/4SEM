import sys
from bitarray import bitarray
from numpy import random



def noise_bits(byte, results, p):
        bits = format(byte, '08b')
        resulting_bits = ''
        for i in range(len(bits)):
            p2 = random.rand()
            if p2 <= p:
                if bits[i] == '1':
                    resulting_bits += '0'
                else:
                    resulting_bits += '1'
            else:
                resulting_bits += bits[i]

        results.append(resulting_bits)
        print(bits, resulting_bits)
if __name__ == "__main__":
    
    results = []
    with open(sys.argv[2], "rb") as f: 
        content = f.read()
        for c in content: 
            noise_bits(c,results,float(sys.argv[1]))

    res = ''.join([str(r) for r in results])
    b = bitarray(res)
    with open(sys.argv[3],'wb') as f:
        b.tofile(f)




