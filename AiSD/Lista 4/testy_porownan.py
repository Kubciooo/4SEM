import hmap
import rbt
import bst 
import time 
import sys


a = hmap.HashMap(47,1000000)
b = rbt.RedBlackTree()
c = bst.BST()
sys.setrecursionlimit(10000)   

n = int(input())
porownaniahmap = 0
porownaniarbt = 0
porownaniabst = 0
polecenia = {"find": 0}
minhmap = 1000000000
minrbt = 1000000000
minbst = 1000000000
maxhmap = 0
maxrbt = 0
maxbst = 0


for i in range(n):
    message = input().split(' ')
    print(i)
    if message[0] == "insert":
        a.insert(message[1])
        b.insert(message[1])
        c.insert(message[1])
    elif message[0] == "find":
        polecenia[message[0]] += 1
        a.find(message[1])
        porownaniahmap+= (a.porownania)
        minhmap = min(minhmap, a.porownania)
        maxhmap = max(maxhmap, a.porownania)
        b.find(message[1])
        porownaniarbt += (b.porownania)
        minrbt = min(minrbt, b.porownania)
        maxrbt = max(maxrbt, b.porownania)
        t3 = time.time()
        c.find(message[1])
        porownaniabst += (c.root.porownania)
        minbst = min(minbst, c.root.porownania)
        maxbst = max(maxbst, c.root.porownania)



print("Średnia ilość porównań hmap: ",porownaniahmap/polecenia["find"])
print("Minimalna ilość porównań hmap: ",minhmap)
print("Maksymalna ilość porównań hmap: ",maxhmap)

print("Średnia ilość porównań rbt: ", porownaniarbt/polecenia["find"])
print("Minimalna ilość porównań rbt: ",minrbt)
print("Maksymalna ilość porównań rbt: ",maxrbt)

print("Średnia ilość porównań bst: ", porownaniabst/polecenia["find"])
print("Minimalna ilość porównań bst: ",minbst)
print("Maksymalna ilość porównań bst: ",maxbst)




