import sys
def porownaj(a,b):
    for i in range(min(len(a),len(b))):
        if a[i].lower() < b[i].lower() or ord(a[i])+32 == ord(b[i]):
            return True
        elif b[i].lower() < a[i].lower() or ord(a[i]) == ord(b[i])+32:
            return False
    if len(a) < len(b):
        return True
    return False


class Node():
    def __init__(self, key):
        self.key = key 
        self.left = self.right = None
        self.porownania = 0
        
    def insert(self,key):
        if porownaj(key, self.key): 
            if self.left is not None:
                self.left.insert(key)
            else: 
                self.left = Node(key)
        
        else:
            if self.right is not None: 
                self.right.insert(key)
            else:
                self.right = Node(key)


    def find(self, key, root):
        if self.key == key:
            root.porownania += 1 
            return self 
        elif porownaj(key,self.key):
            root.porownania += 3
            if self.left is None: 
                return None 
            else: 
                return self.left.find(key,root)
        else: 
            root.porownania += 4
            if self.right is None: 
                return None
            else: 
                return self.right.find(key,root)
    
    def min(self):
        if self is None: 
            return self
        if self.left is not None: 
            return self.left.min()
        else: 
            return self
    
    def max(self):
        if self is None:
            return self
        if self.right is not None: 
            return self.right.max()
        else:
            return self

    def inorder(self):
        if self is not None: 
            if self.left is not None: 
                self.left.inorder()
            print(self.key, end = ' ')
            if self.right is not None: 
                self.right.inorder()

    def delete(self, key):
        if self is None: 
            return self
        if porownaj(key, self.key):
            if self.left is not None:
                self.left = self.left.delete(key)

        elif porownaj(self.key,key):
            if self.right is not None:
                self.right = self.right.delete(key)
        
        else: 
            if self.left is None: 
                temp = self.right
                self = None
                return temp
            elif self.right is None: 
                temp = self.left
                self = None
                return temp

            temp = self.right.min()
            self.key = temp.key
            self.right = self.right.delete(temp.key)
        return self
    
    def successor(self, k):
        if porownaj(self.key,k):
            return self.right.successor(k)
        elif porownaj(k,self.key):
            if self.left.key == k: 
                return self.key
            else: 
                return self.left.successor(k)


class BST():
    def __init__(self):
        self.root = None
        self.MAX_LEN = 0 
        self.ACT_LEN = 0


    def insert(self, key):
        self.ACT_LEN += 1 
        self.MAX_LEN = max(self.ACT_LEN, self.MAX_LEN)
        if self.root is None: 
            self.root = Node(key)
        else:
            self.root.insert(key) 


    def find(self, key):
        if self.root is not None: 
            self.root.porownania = 0
            f = self.root.find(key, self.root)
            if f is not None: 
                return 1
            else:
                return 0

    def delete(self,key):
        if self.find(key) == 1: 
            self.ACT_LEN -= 1
            if self.root is not None: 
                self.root = self.root.delete(key)

    def inorder(self):
        if self.root is not None:
            self.root.inorder()
        print()
    def min(self):
        if self.root is None: 
            return None
        else:
             return self.root.min().key
    def max(self):
        if self.root is None:
            return None
        else:
            return self.root.max().key
    def successor(self, k):
        if self.root is not None: 
            n = self.root.find(k,self.root)
            if n is None or self.max() == k:
                return None
            else:
                if n.right is not None: 
                    return n.right.min().key
                else:  
                    return self.root.successor(k)

def cut(message):
    key = message
    while len(key) > 0 and not key[0].isalpha():
        key = key[1:]
    while len(key) > 0 and not key[-1].isalpha():
        key = key[:-1]
    return key

def main():
    a = BST()
    sys.setrecursionlimit(10000)   
    polecenia = {"max": 0, "min":0, "inorder":0, "insert":0, "delete":0, "find":0, "load":0, "successor": 0}
    n = int(input())
    for _ in range(n):
        message = input().split(" ")
        message[0] = message[0].replace('\r','')
        if len(message) == 2:
            message[1] = message[1].replace('\r','')
        polecenia[message[0]] += 1
        if message[0] == "max": 
            print(a.max() if a.max() is not None else '')
        elif message[0] == "min":
            print(a.min() if a.min() is not None else '')
        elif message[0] == "inorder":
            a.inorder()
        elif message[0] == "insert":
            a.insert(cut(message[1]))
        elif message[0] == "delete":
            a.delete(cut(message[1]))
        elif message[0] == "find":
            print(a.find(cut(message[1])))
        elif message[0] == "load":
            try:
                with open(message[1],'r') as f:
                    content = f.read()
                    for x in content.split():
                        polecenia['insert'] += 1
                        a.insert(cut(x))
            except IOError: 
                print("Nie udało się wczytać pliku")
        elif message[0] == "successor":
            key = cut(message[1])
            temp = a.successor(key)
            if temp == None:
                print()
            else:
                print(temp)
    print("ilość wykonań: ",polecenia, file=sys.stderr)
    print("Maksymalna wielkość: ",a.MAX_LEN,file=sys.stderr)
if __name__ == '__main__':
    main()
    