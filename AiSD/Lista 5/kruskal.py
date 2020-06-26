from zad1 import PriorityQueue
import sys

class Graph(object):
    def __init__(self, n):
        self.edges = PriorityQueue()
        self.n = n
    

    def add_edge(self, u, v, w):
        self.edges.insert((w,u,v))
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else: 
            parent[yroot] = xroot
            rank[xroot] += 1

    def mst(self):
        parent = [i for i in range(self.n+1)]
        rank = [0]*(self.n+1)
        result_edges = []
        taken_edges = 0 
        while taken_edges < self.n - 1: 
            (w,u,v) = self.edges.pop()
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y: 
                taken_edges += 1
                result_edges.append((u,v,w))
                self.union(parent, rank, x, y)

        return result_edges



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
    
    start = int(input())
    edges = g.mst()
    edges.sort()
    size = 0
    for ((v, u, w)) in edges:
        if u != -1: 
            print(min(u,v), max(u,v), w)
            size += w

    print(size)

