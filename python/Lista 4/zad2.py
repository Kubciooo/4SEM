import random

def tree(max_n, n = 1):

    def generate(value, max_n, n = 1, gotMax = False):
        node = []
        node.append(value)
        node.append(None)
        node.append(None)
        if n == max_n:
            gotMax = True
            return node, gotMax
        left = random.random()
        if left > 0.5: 
            node[1], gotMax = generate(2*value, max_n, n+1, gotMax)
        if not gotMax:
            node[2], gotMax = generate(2*value+1, max_n, n+1, gotMax) 
        else:
            right = random.random()
            if right > 0.5:
                node[2], gotMax = generate(2*value+1, max_n, n+1, gotMax) 
        return node, gotMax
    
    def function(node, value = 1):
        l = []
        l.append(node)
        while l:
            act = l.pop(0)
            act[0] = str(value) 
            value += 1
            if act[1] is not None:
                l.append(act[1])
            if act[2] is not None:
                l.append(act[2])
    n, m = generate(1,max_n)
    function(n)
    return n



def dfs(node, values=[]):
    values.append(node[0])
    if node[1] == None and node[2] == None:
        return
    if node[1] is not None : dfs(node[1],values)
    if node[2] is not None : dfs(node[2],values)
    return values

def bfs(node, list = [], values = []):
    list.append(node)
    while list: 
        n = list.pop(0)
        values.append(n[0])
        if n[1] != None: 
            list.append(n[1])
        if n[2] != None:
            list.append(n[2])
    return values


n = tree(5)
print(n)
a = dfs(n)
b = bfs(n)
print(a)
print(b)
