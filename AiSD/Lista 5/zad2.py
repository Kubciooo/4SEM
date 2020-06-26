from zad1 import PriorityQueue
import sys
from timeit import default_timer as timer



class Graph(object):
    def __init__(self, n):
        self.vertices = { i : [] for i in range(1,n+1)}
        self.n = n
    
    def neighbors(self, v):
        return list(self.vertices[v])

    def add_edge(self, u, v, w):
        self.vertices[u].append((v,w))
    

    def dijkstra(self, start):
        q = PriorityQueue()
        values = {i : 10000000000.0 for i in range(1,self.n+1)}
        values[start] = 0
        parent = {}
        parent[start] = start
        q.insert((0,start))
        
        while not q.empty():
            (cost, u) = q.pop()
            for (v,w) in self.neighbors(u):
                if values[v] > values[u] + w: 
                    values[v] = values[u] + w
                    parent[v] = u 
                    q.insert((values[v], v))
        return values, parent




def read_parents(i,start, parent,values):
    path = []
    while i != start: 
        path.append((parent[i], values[(parent[i],i)], i))
        i = parent[i]
    path.reverse()
    return path


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
    t1 = timer()*100
    results, parent = g.dijkstra(start)
    print("Czas wykonania w ms:", timer()*100-t1,file=sys.stderr)
    for (k,v) in results.items():
        print(k,v)
    for i in range(1,n+1):
        print(i,":",read_parents(i,start,parent, prices),file=sys.stderr)
