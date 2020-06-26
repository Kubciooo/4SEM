from zad1 import PriorityQueue
import sys

class Graph(object):
    def __init__(self, n):
        self.vertices = { i : [] for i in range(1,n+1)}
        self.n = n
    
    def neighbors(self, v):
        return list(self.vertices[v])

    def add_edge(self, u, v, w):
        self.vertices[u].append((v,w))
        self.vertices[v].append((u,w))
    
    def mst(self):
        start = 1
        q = PriorityQueue()
        values = {i : 100000000.0 for i in range(1,self.n+1)}
        values[start] = 0
        q.insert((0,start))
        mstSet = [False for _ in range(self.n+1)]
        mstSet[start] = True
        parent = {}
        edges = []
        parent[start] = start
        while not q.empty():
            (cost, u) = q.pop()
            edges.append((parent[u] ,u, cost))
            for (v,w) in self.neighbors(u):
                if values[v] >  w: 
                    values[v] =  w
                    parent[v] = u
                    q.priority(v, w)
                if mstSet[v] == False:
                    q.insert((values[v],v))
                    mstSet[v] = True
        return edges




if __name__ == "__main__":
    n = int(input())
    m = int(input())
    g = Graph(n)
    prices = {}
    for i in range(m):
        (u,v,w) = input().split(' ')
        u = u.replace('\r','')
        v = v.replace('\r','')
        w = w.replace('\r','')
        u = int(u)
        #u+=1
        v = int(v)
        #v+=1
        w = float(w)
        prices[(u,v)] = w
        g.add_edge(u,v,w)
    
    edges = g.mst()
    edges.sort()
    size = 0
    for ((v, u, w)) in edges[1:]:
        if u != -1: 
            print(min(u,v), max(u,v), w)
            size += w

    print(size)

