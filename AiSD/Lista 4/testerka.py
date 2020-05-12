import time 
import hmap
import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generuj_plik():
    print("1000000")
    for i in range(500000): 
        print("insert " + randomString(5))
    for i in range(500000):
        print("delete " +randomString(5))
        










# generuj_plik()
MIN_T = (10000,0)
for i in range(1,1000):
    t0 = time.clock()
    hashmap = hmap.HashMap(i,1000000)
    with open("testowy.txt","r") as f: 
        content = f.readlines()
    n = int(content[0])
    for c in content[1:]:
        message = c.split(" ")
        if message[0] == "insert":
            hashmap.insert(message[1])
        elif message[0] == "delete":
            hashmap.delete(message[1])

    t1 = time.clock()
    #print(i, ": ",t1-t0)
    if t1 - t0 < MIN_T[0]:
        MIN_T = (t1-t0, i) 
    print(MIN_T)







