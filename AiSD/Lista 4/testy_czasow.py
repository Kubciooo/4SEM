import hmap
import rbt
import bst 
import time 




a = hmap.HashMap(47,1000000)
b = rbt.RedBlackTree()
c = bst.BST()

n = int(input())
czasyhmap = {"insert": 0, "find": 0, "delete": 0}
czasyrbt = {"insert": 0, "find": 0, "delete": 0}
czasybst = {"insert": 0, "find": 0, "delete": 0}
polecenia = {"insert": 0, "find": 0, "delete": 0}

for i in range(n):
    print(i)
    message = input().split(' ')
    polecenia[message[0]] += 1
    if message[0] == "insert":
        t1 = time.time()
        a.insert(message[1])
        czasyhmap[message[0]] += (time.time() - t1)
        t2 = time.time()
        b.insert(message[1])
        czasyrbt[message[0]] += (time.time() - t1)
        t3 = time.time()
        c.insert(message[1])
        czasybst[message[0]] += (time.time() - t1)
    elif message[0] == "find":
        t1 = time.time()
        a.find(message[1])
        czasyhmap[message[0]] += (time.time() - t1)
        t2 = time.time()
        b.find(message[1])
        czasyrbt[message[0]] += (time.time() - t1)
        t3 = time.time()
        c.find(message[1])
        czasybst[message[0]] += (time.time() - t1)
    else:
        t1 = time.time()
        a.delete(message[1])
        czasyhmap[message[0]] += (time.time() - t1)
        t2 = time.time()
        b.delete(message[1])
        czasyrbt[message[0]] += (time.time() - t1)
        t3 = time.time()
        c.delete(message[1])
        czasybst[message[0]] += (time.time() - t1)

print("Insert:\nŚredni czas hmap: ",czasyhmap["insert"]/polecenia["insert"])
print("Średni czas rbt: ", czasyrbt["insert"]/polecenia["insert"])
print("Średni czas bst: ", czasybst["insert"]/polecenia["insert"])

print("Find:\nŚredni czas hmap: ",czasyhmap["find"]/polecenia["find"])
print("Średni czas rbt: ", czasyrbt["find"]/polecenia["find"])
print("Średni czas bst: ", czasybst["find"]/polecenia["find"])

print("Delete:\nŚredni czas hmap: ",czasyhmap["delete"]/polecenia["delete"])
print("Średni czas rbt: ", czasyrbt["delete"]/polecenia["delete"])
print("Średni czas bst: ", czasybst["delete"]/polecenia["delete"])







