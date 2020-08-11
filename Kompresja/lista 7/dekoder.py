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

def decode(byte):
    data = format(byte, '08b')
    data = list(data)
    D1 = data[2]
    D2 = data[4]
    D3 = data[5]
    D4 = data[6]    
    C1 = data[0]
    s1 = (int(C1) + int(D1) + int(D2) + int(D4)) % 2
    C2 = data[1]
    s2 = (int(C2) + int(D1) + int(D3) + int(D4)) % 2
    C3 = data[3]
    s3 = (int(C3) + int(D2) + int(D3) + int(D4)) % 2
    C4 = data[7]
    res = ''.join([str(s3),str(s2),str(s1)])

    p = sum(map(int, data)) % 2

    syndrome = int(res,2)
    if syndrome == 0 and p == 0:
        return ''.join(map(str,[data[2],data[4],data[5],data[6]])), 0
    
    if syndrome != 0 and p == 1: 
        data[syndrome-1] = '0' if data[syndrome-1] == '1' else '1'
        return ''.join(map(str,[data[2],data[4],data[5],data[6]])), 1
    
    if syndrome != 0 and p == 0: 
        return ''.join(map(str,[data[2],data[4],data[5],data[6]])), 2

    if syndrome == 0 and p == 1:
        return ''.join(map(str,[data[2],data[4],data[5],data[6]])), 1
     
    

if __name__ == "__main__":
    
    results = ''
    errors = 0
    with open(sys.argv[1], "rb") as f: 
        content = f.read()
        for c in content: 
            x = decode(c)
            results += x[0]
            errors += 1 if x[1] == 2 else 0

    print(f"{errors} podwójnych błędów")

    b = bitarray(results)

    # res = ''.join([str(r) for r in results])
    # b = bitarray(res)
    with open(sys.argv[2],'wb') as f:
        b.tofile(f)




