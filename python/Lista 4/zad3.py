import random
import numpy as np


class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

def tree(max_n, max_children, n = 1):
    value = 2  #value - numer wierzchołka co mu przypisujemy 
    node = Node(1)
    t =[node, 1] # node - wierzchołek, 1 bo na początku mamy n równe 1
    how_many = np.zeros(max_n+1, dtype=int) # tablica zawierająca info ile wierzchołków na którym poziomie jest 
    how_many[1] = 1
    treeList = []
    treeList.append(t)
    while treeList: 
        act, p = treeList.pop(0)
        m = 0
        if p != max_n:
            if how_many[p+1] == 0 and ( (len(treeList) != 0 and treeList[0][1] != p) or len(treeList) == 0):
                print(act.value," jest ostatnim dziekiem i jego rodzeństwo nie ma dzieci! Więc on musi mieć 1 dziecko minimum")
                m = 1
            number_of_children = random.randint(m, max_children)
            how_many[p+1] += number_of_children
            for i in range(number_of_children):
                child = Node(value)
                act.children.append(child)
                value += 1
                t = [child,p+1]
                treeList.append(t)
            print("OJCIEC:", act.value, "dzieci: ", end = " ")
            for child in act.children:
                print(child.value, " ",end=" ")
            print()
    return node


        


def dfs(node):
    print(node.value, end=" ")
    for child in node.children:
        dfs(child)
def bfs(node):
    list = []
    list.append(node)
    while list:
        n = list.pop(0)
        print(n.value, end=" ")
        for child in n.children:
            list.append(child)


        
x = tree(3,3)
print()
bfs(x)
print()
dfs(x)
