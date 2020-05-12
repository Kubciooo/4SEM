import sys
from rbt import RedBlackTree



class HashMap():
    def __init__(self, MAX_THRESHOLD, HASHMAP_LEN):
        self.MAX_LEN = 0
        self.ACT_LEN = 0
        self.HASHMAP_LEN = min(1000000,10*HASHMAP_LEN)
        self.hash_table = [("table",[]) for i in range(self.HASHMAP_LEN)]
        self.MAX_THRESHOLD = MAX_THRESHOLD 
        self.porownania = 0
    def insert(self, key):
        self.ACT_LEN += 1
        self.MAX_LEN = max(self.MAX_LEN, self.ACT_LEN)
        hashed_key = hash(key)%self.HASHMAP_LEN
        if self.hash_table[hashed_key][0] == "table":
            self.hash_table[hashed_key][1].append(key)
            self.MAX_LEN = max(self.MAX_LEN, len(self.hash_table[hashed_key][1]))
            if len(self.hash_table[hashed_key][1]) > self.MAX_THRESHOLD: 
                tree = RedBlackTree()
                for key in self.hash_table[hashed_key][1]:
                    tree.insert(key)
                self.hash_table[hashed_key] = ("tree", tree)
        else: 
            self.hash_table[hashed_key][1].insert(key)
            self.MAX_LEN = max(self.MAX_LEN, self.hash_table[hashed_key][1].MAX_LEN)


    def find(self, key):
        self.porownania = 0
        hashed_key = hash(key)%self.HASHMAP_LEN
        if self.hash_table[hashed_key][0] == "table": 
            for i in range(len(self.hash_table[hashed_key][1])):
                self.porownania += 1
                if self.hash_table[hashed_key][1][i] == key: 
                    return 1
            return 0
        else: 
            temp = self.hash_table[hashed_key][1].find(key).key
            self.porownania = self.hash_table[hashed_key][1].porownania
            return 0 if temp == 0 else 1
    
    def delete(self, key):
        hashed_key = hash(key)%self.HASHMAP_LEN
        if self.hash_table[hashed_key][0] == "table": 
            if key in self.hash_table[hashed_key][1]: 
                self.ACT_LEN -= 1
                self.hash_table[hashed_key][1].remove(key)
        else: 
            temp = self.hash_table[hashed_key][1].ACT_LEN
            self.hash_table[hashed_key][1].delete(key)
            if temp > self.hash_table[hashed_key][1].ACT_LEN:
                self.ACT_LEN -= 1
            keys = self.hash_table[hashed_key][1].inorder().split()
            if len(keys) <= self.MAX_THRESHOLD: 
                new_list = [k for k in keys]
                self.hash_table[hashed_key] = ("table", new_list)

        
    def min(self):
        return ''
    
    def max(self):
        return ''
    
    def inorder(self):
        return ''
    
    def succesor(self):
        return ''

    def print_all_data(self):
        for i in range(self.HASHMAP_LEN):
            if self.hash_table[i][0] == "table":
                if len(self.hash_table[i][1]) > 0: 
                    print(self.hash_table[i])
            else:
                print(f"('{self.hash_table[i][0]}',[",end='')
                print(self.hash_table[i][1].inorder(), end='')
                print("])")


def cut(message):
    key = message
    while len(key) > 0 and not key[0].isalpha():
        key = key[1:]
    while len(key) > 0 and not key[-1].isalpha():
        key = key[:-1]
    return key
    
def main():
    polecenia = {"max": 0, "min":0, "inorder":0, "insert":0, "delete":0, "find":0, "load":0, "successor":0}
    n = int(input())
    hmap = HashMap(47,n) 
    for _ in range(n):
        message = input().split(" ")
        message[0] = message[0].replace('\r','')
        if len(message) == 2:
            message[1] = message[1].replace('\r','')
        polecenia[message[0]] += 1
        if message[0] == "max": 
             print(hmap.max())
        elif message[0] == "min":
            print(hmap.min())
        elif message[0] == "inorder" or message[0] == "successor":
            print()
        elif message[0] == "insert":
            hmap.insert(cut(message[1]))
        elif message[0] == "delete":
            hmap.delete(cut(message[1]))
        elif message[0] == "find":
            print(hmap.find(cut(message[1])))
        elif message[0] == "load":
            try:
                with open(message[1],'r') as f:
                    content = f.read()
                    for x in content.split():
                        polecenia['insert'] += 1
                        hmap.insert(cut(x))
            except IOError: 
                print("Nie udało się wczytać pliku")
    print("ilość wykonań: ",polecenia, file=sys.stderr)
    print("Maksymalna wielkość: ",hmap.MAX_LEN,file=sys.stderr)



if __name__ == "__main__":
    main()
