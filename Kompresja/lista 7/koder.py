import sys
from bitarray import bitarray
def xorOfArray(arr, n): 
        xor_arr = 0
        for i in range(n): 
    
            xor_arr = xor_arr ^ arr[i] 
    
        # Return the XOR 
        return xor_arr


def split_bits(byte):
        bits = format(byte, '08b')
        bits_one = bits[:4]
        bits_two = bits[4:]
        return bits_one, bits_two

def code_bits(data):
    D = [int(d) for d in data]
    
    C1 = xorOfArray([D[0],D[1],D[3]],3)
    C2 = xorOfArray([D[0],D[2],D[3]],3)
    C3 = xorOfArray([D[1],D[2],D[3]],3)
    C4 = xorOfArray([C1,C2,D[0],C3,D[1],D[2],D[3]],7)
    Code = [C1,C2,D[0],C3,D[1],D[2],D[3],C4]
    result = (''.join([str(c) for c in Code])) 
    return result

def code_byte(byte, results):
    b1, b2 = split_bits(byte)
    results.append(code_bits(b1))
    results.append(code_bits(b2))

if __name__ == "__main__":
    
    results = []
    with open(sys.argv[1], "rb") as f: 
        content = f.read()
        for c in content: 
            code_byte(c,results)

    res = ''.join([str(r) for r in results])
    b = bitarray(res)
    with open(sys.argv[2],'wb') as f:
        b.tofile(f)




