# Implementing Red-Black Tree in Python

import sys
import re

def porownaj(a,b):
    for i in range(min(len(a),len(b))):
        if a[i].lower() < b[i].lower() or ord(a[i])+32 == ord(b[i]):
            return True
        elif b[i].lower() < a[i].lower() or ord(a[i]) == ord(b[i])+32:
            return False
    if len(a) < len(b):
        return True
    return False
    #return a < b



class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class RedBlackTree():
    def __init__(self):
        #W RB Tree mamy powiedziane, że wszystkie liście "NULLowe" są czarne, więc zamiast za każdym razem tworzyć taki liść od podstaw - zróbmy sobie po prostu taki obiekt"
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.MAX_LEN = 0 
        self.ACT_LEN = 0 
        self.porownania = 0 
    def min(self, node):
        if node == self.TNULL: 
            return node
        while node.left != self.TNULL:
            node = node.left
        return node
    
    def max(self, node):
        if node == self.TNULL:
            return node
        while node.right != self.TNULL:
            node = node.right
        return node

    def find(self, key):
        self.porownania = 0
        x = self.root
        while x != self.TNULL and x.key != key:  # dopóki nie trafimy do TNULLA szukamy miejsca, w którym wstawimy naszego node
            self.porownania += 1
            if porownaj(key,x.key):
                x = x.left
            else:
                x = x.right
        return x 

    def insert(self, key):
        #najpierw przeprowadzamy typowy insert z bst, tylko tutaj dodajemy kolory i nasze liście TNULL
        node = Node(key) # tworzymy nowy obiekt 
        node.left = self.TNULL # jego dzieci to będą TNULLe
        node.right = self.TNULL
        node.parent = None
        node.key = key
        node.color = 1 # po standardowym insercie nasz node będzie czerwony, więc już ustawmy jego kolor na czerwień 
        self.ACT_LEN += 1 
        self.MAX_LEN = max(self.MAX_LEN, self.ACT_LEN)
        y = None # zmienna pomocnicza, y to ojciec x 
        x = self.root

        while x != self.TNULL:  # dopóki nie trafimy do TNULLA szukamy miejsca, w którym wstawimy naszego node
            y = x
            if porownaj(node.key,x.key):
                x = x.left
            else:
                x = x.right

        node.parent = y #wyszliśmy z while, czyli jesteśmy na odpowiednim liściu - ojcem naszego node będzie ojciec x

        if y == None: #ale jeżeli ojciec jest pusty, to znaczy, że jesteśmy na roocie - więc musimy ustawić naszego node jako roota drzewa
            self.root = node
        elif porownaj(node.key,y.key): # chcemy zobaczyć teraz którym synem y jest nasz node
            y.left = node
        else:
            y.right = node

        if node.parent == None: #jeżeli node był rootem, to nie musimy kolorować ani przeprowadzać rotacji
            node.color = 0 # root zawsze ma kolor czarny 
            return

        if node.parent.parent == None: # to samo jeżeli nasz node jest dzieckiem roota, bo wtedy root nie ma brata, czyli node nie ma wujka  
            return

        self.fix_insert(node) # teraz kolorujemy i przeprowadzamy rotacje 


    def fix_insert(self, k):
        #dopóki ojciec naszego nowo dodanego node o nazwie 'k' jest czerwony: 
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right: # znajdźmy brata naszego ojca
                u = k.parent.parent.left #u - brat ojca k 
                if u.color == 1: # jeżeli kolor wujka jest czerwony: 
                    u.color = 0 # 1) zmieniamy kolor wujka i ojca na czarny,
                    k.parent.color = 0
                    k.parent.parent.color = 1 #2) zmieniamy kolor dziadka na czerwony
                    k = k.parent.parent #3) robimy fix_insert() dla dziadka 
                else: # jeżeli brat ojca jest czarny: 
                    if k == k.parent.left: #right left case - k jest lewym synem ojca, ojciec k jest prawym synem swojego ojca 
                        k = k.parent #right left case: przeprowadź right roration k i dla wyniku wykonaj right right case
                        self.right_rotate(k) 
                    k.parent.color = 0 # przy right right case zmieniamy kolory ojca i dziadka 
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent) # right right case - k jest prawym synem ojca, a ojciec k jest prawym synem swojego ojca 
                                                    # right right case: wykonaj left rotation i zmień kolorami ojca i dziadka(wiemy, że ojciec jest czerwony)
            else:
                u = k.parent.parent.right # teraz nasz ojciec jest lewym synem

                if u.color == 1:# to samo - dopóki wujek ma kolor czerwony, to: 
                    u.color = 0 # pokoloruj ojca i wujka na czarno
                    k.parent.color = 0 
                    k.parent.parent.color = 1 #pokoloruj dziadka na czerwono 
                    k = k.parent.parent  # wykonaj fix_insert dla dziadka 
                else: # jak wujek jest czarny: 
                    if k == k.parent.right: # left right case - k jest prawym synek ojca, ojciec jest lewym synem swojego ojca  
                        k = k.parent   # left right case: wykonaj left rotation i left left case 
                        self.left_rotate(k)
                    k.parent.color = 0 # przy left left case zamień kolory ojca i dziadka, wiemy, że ojciec ma kolor czerwony 
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent) # left left case - wykonaj righ rotation i zmień kolory ojca i dziadka 
            if k == self.root: # jeżeli doszliśmy już do roota, to kończymy pętlę 
                break
        self.root.color = 0 # root ma zawsze być czarny! 
    

    def delete(self, key):
        self.delete_2(self.root, key)

    def delete_2(self, node, key):
        # Po pierwsze szukamy elementu, który chcemy usunąć 
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node
            if porownaj(key, node.key):
                node = node.left
            else:
                node = node.right

        if z == self.TNULL:
            return
    
        self.ACT_LEN -= 1
        self.MAX_LEN = max(self.ACT_LEN, self.MAX_LEN)
        #przeprowadzamy standardowe usuwanie elementu z bst 
        y = z
        y_original_color = y.color
        #jeżeli z ma tylko jednego syna, to prosto usuwamy z 
        if z.left == self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.transplant(z, z.left)
        else:
            #jeżeli mamy 2 synów, to chcemy zastąpić 'z' jego succesorem, a successora chcemy usunąć 
            y = self.min(z.right)
            y_original_color = y.color # potrzebujemy kolor node'a do usunięcia, żeby potem w razie potrzeby naprawić kolory drzewa 
            #potrzebujemy znać kolor node'a, który usuwamy 
            x = y.right # x to jest node, którym zastąpiliśmy naszego usuniętego node'a 
            if y.parent == z: 
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0: #jeżeli usunęliśmy czarnego node'a, to znaczy, że jest istnieje możliwośc, że zaburzyliśmy głębokość czarnych wierzchołków, więc musimy to sprawdzić
            self.delete_fix(x)

    def delete_fix(self, x):
        #jeżeli zarówno usunięty node, jak i ten, którym go zastąpiliśmy są czarne, to x jest podwójnie czarny. Musimy go więc zredukować do zwykłego czarnego:
        #dopóki x jest czarny i nie jest rootem: 
        while x != self.root and x.color == 0:
            if x == x.parent.left: # jeżeli x jest lewym synek
                s = x.parent.right
                if s.color == 1: # jeżeli brat x jest czerwony, to musimy przeprowadzić rotację i zmienić kolorami brata i ojca - ojciec będzie teraz czerwony, a brat czarny
                    s.color = 0 # Po czym przeprowadzamy right case: robimy left rotate na ojcu 
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right # ustawiamy w 's' nowego brata 'x'. Uwaga! Nowy 's' zawsze będzie koloru czarnego! 
                
                #poniżej wiemy, że s jest czarny 
                if s.left.color == 0 and s.right.color == 0: # jeżeli obaj synowie naszego brata mają kolor czarny, to ten brat musi mieć kolor czerwony 
                    s.color = 1
                    x = x.parent # idziemy do góry 
                else: # jeżeli któryś z synów s jest czerwony, to musimy przeprowadzić rotację 
                    # s jest prawym synem, więc mamy albo right right case albo right left case: 
                    if s.right.color == 0: # skoro prawy syn jest czarny, to mamy right left 
                        s.left.color = 0   #  ustawmy kolor lewego syna na czarny
                        s.color = 1 # a kolor s na czerwony
                        self.right_rotate(s) # wywołajmy right rotation 
                        s = x.parent.right #zaktualizujmy s 

                    s.color = x.parent.color #right right case 
                    x.parent.color = 0 
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left

                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left 

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
    #funkcja pomocnicza, podmieniamy u na v w naszym drzewie 
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

 
    def get_root(self):
        return self.root


    def inorder_2(self, node):
        s = ""
        if node != self.TNULL:
            s += self.inorder_2(node.left)
            s += node.key
            s+= " "
            s+= self.inorder_2(node.right)
        return s

    def inorder(self):
        return self.inorder_2(self.root)

    def successor(self, k):
        x = self.find(k)
        if x == self.TNULL: 
            return None 
        
        if x.right != self.TNULL:
            return self.min(x.right)

        y = x.parent
        while y != None and y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

def cut(message):
    key = message
    while len(key) > 0 and not key[0].isalpha():
        key = key[1:]
    while len(key) > 0 and not key[-1].isalpha():
        key = key[:-1]
    return key

def main():
    bst = RedBlackTree()
    polecenia = {"max": 0, "min":0, "inorder":0, "insert":0, "delete":0, "find":0, "load":0, "successor":0}
    n = int(input())
    for _ in range(n):
        message = input().split(" ")
        message[0] = message[0].replace('\r','')
        if len(message) == 2:
            message[1] = message[1].replace('\r','')
        polecenia[message[0]] += 1
        if message[0] == "max": 
            print(bst.max(bst.root).key if bst.get_root() != bst.TNULL else '')
        elif message[0] == "min":
            print(bst.min(bst.root).key if bst.get_root() != bst.TNULL else '')
        elif message[0] == "inorder":
            print(bst.inorder())
        elif message[0] == "insert":
            key = message[1]
            bst.insert(cut(key))
        elif message[0] == "successor":
            key = cut(message[1])
            temp = bst.successor(key)
            if temp == None or temp == bst.TNULL:
                print()
            else:
                print(temp.key)

        elif message[0] == "delete":
            bst.delete(cut(message[1]))
        elif message[0] == "find":
            print(0 if bst.find(cut(message[1])).key == 0 else 1)
        elif message[0] == "load":
            try:
                with open(message[1],'r') as f:
                    content = f.read()
                    for x in content.split():
                        polecenia['insert'] += 1
                        bst.insert(cut(x))
            except IOError: 
                print("Nie udało się wczytać pliku")



    print("ilość wykonań: ",polecenia, file=sys.stderr)
    print("Maksymalna wielkość: ",bst.MAX_LEN,file=sys.stderr)

if __name__ == '__main__':
    main()
    