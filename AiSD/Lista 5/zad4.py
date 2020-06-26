import numpy as np
import sys
from zad1 import PriorityQueue
import kruskal
import time
class Graph(object):
    def __init__(self, n):
        self.vertices = { i : [] for i in range(1,n+1)}
        self.edges = []
        self.n = n
    
    def neighbors(self, v):
        return list(self.vertices[v])

    def add_edge(self, u, v, w):
        self.vertices[u].append((v,w))
        self.vertices[v].append((u,w))
        self.edges.append((u,v,w))

    def __str__(self):
        s = ''
        for i in range(1,self.n+1):
             s += str(i)
             s += ': '
             s += str(self.vertices[i])
             s += '\n'
        return s


    def random_neighbor(self,v):
        random_n = np.random.randint(0,len(self.neighbors(v)))
        return self.vertices[v][random_n]

    def random_traversal(self):
        start_time = time.time()
        path = []
        v = np.random.randint(1,self.n+1)
        visited = [False for i in range(self.n+1)]
        visited[v] = True
        vis = 1
        final_cost = 0
        steps_size = 1
        while vis < self.n:
            steps_size += 1
            next_one = self.random_neighbor(v)
            path.append(str(v)+'-->'+str(next_one[0])+" koszt: "+str(next_one[1]))
            if not visited[next_one[0]]:
                visited[next_one[0]] = True
                vis += 1
            final_cost += next_one[1]
            v = next_one[0]
        print("Losowe przechodzenie:\n",'\n'.join(path),'\n',file=sys.stderr)
        print("LOSOWE PRZECHODZENIE")
        print("Kroki: ",steps_size, ' koszt: ',final_cost,' Pamięć: ',sys.getsizeof(visited),'B',' czas: ',time.time()-start_time,'s',sep='')
        print()



    def traverse_using_min_weight(self):
        start_time = time.time()
        path = []
        v = np.random.randint(1,self.n+1)
        visited = [v]
        final_cost = 0
        steps_size = 1
        while len(visited) < self.n:
            steps_size += 1
            (min_index, min_cost) = self.vertices[v][0]
            for i in range(len(self.vertices[v])):
                (act_index, act_cost) = self.vertices[v][i]
                if act_cost < min_cost and act_index not in visited: 
                    (min_index, min_cost) = (act_index, act_cost)
            path.append(str(v)+'-->'+str(min_index)+" koszt: "+str(min_cost))
            visited.append(min_index)
            final_cost += min_cost
            v = min_index
        print("Minimalne wagi:\n",'\n'.join(path),'\n',file=sys.stderr)
        print("MINIMALNE WAGI")
        print("Kroki: ",steps_size, ' koszt: ',final_cost,' Pamięć: ',sys.getsizeof(visited)+sys.getsizeof(act_index)+sys.getsizeof(min_cost),'B',' czas: ',time.time()-start_time,'s',sep='')
        print()

    def prim_mst(self):
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


    def dfs(self, v, parent, edges,path,steps_size):
        steps_size[0] += 1
        path.append(v)
        for (index, _) in edges[v]:
            if index == parent: 
                continue
            self.dfs(index, v, edges,path,steps_size)
        steps_size[0] += 1


    def get_cost(self,u,v):
        return [self.vertices[u][i][1] for i in range(len(self.vertices[u])) if self.vertices[u][i][0] == v ][0]

    def traverse_using_prim(self):
        start_time = time.time()
        edges = self.prim_mst()[1:]
        final_cost = 0
        steps_size = [0]
        path = []
        dfs_path = []
        new_graph = {i : [] for i in range(self.n+1)}
        for (u,v,w) in edges:
            new_graph[u].append((v,w))
            new_graph[v].append((u,w))
        starting_v = np.random.randint(1,self.n+1)
        self.dfs(starting_v,starting_v,new_graph,dfs_path,steps_size)
        for i in range(len(dfs_path)-1):
            c = self.get_cost(dfs_path[i],dfs_path[i+1])
            path.append(str(dfs_path[i])+'-->'+str(dfs_path[i+1])+" koszt: "+str(c))
            final_cost += c


        print("Prim:\n",'\n'.join(path),'\n',file=sys.stderr,sep='')
        print("PRIM")
        print(sum([e[2] for e in edges]))
        print("Kroki: ",steps_size[0], ' koszt: ',final_cost,' Pamięć: ',sys.getsizeof(edges)+sys.getsizeof(new_graph),'B',' czas: ',time.time()-start_time,'s',sep='')
        print()

    def traverse_using_kruskal(self):
        start_time = time.time()
        g2 = kruskal.Graph(self.n)
        for (u,v,w) in self.edges:
            g2.add_edge(u,v,w)

        edges = g2.mst()
        final_cost = 0
        steps_size = [0]
        path = []
        dfs_path = []
        new_graph = {i : [] for i in range(self.n+1)}
        for (u,v,w) in edges:
            new_graph[u].append((v,w))
            new_graph[v].append((u,w))
        starting_v = np.random.randint(1,self.n+1)
        self.dfs(starting_v,starting_v,new_graph,dfs_path,steps_size)
        for i in range(len(dfs_path)-1):
            c = self.get_cost(dfs_path[i],dfs_path[i+1])
            path.append(str(dfs_path[i])+'-->'+str(dfs_path[i+1])+" koszt: "+str(c))
            final_cost += c

        print("KRUSKAL:\n",'\n'.join(path),'\n',file=sys.stderr,sep='')
        print("KRUSKAL")
        print(sum([e[2] for e in edges]))
        print("Kroki: ",steps_size[0], ' koszt: ',final_cost,' Pamięć: ',sys.getsizeof(edges)+sys.getsizeof(new_graph)+sys.getsizeof(g2),'B',' czas: ',time.time()-start_time,'s',sep='')
        print()      
        

def create_random_graph():
    n = int(input())
    m = int(n*(n-1)/2)
    g = Graph(n)
    for _ in range(m):
        (u,v,w) = input().split(' ')
        u = u.replace('\r','')
        v = v.replace('\r','')
        w = w.replace('\r','')
        u = int(u)
        #u+=1
        v = int(v)
        #v+=1
        w = float(w)
        g.add_edge(u,v,w)
    return g


if __name__ == "__main__":
    g = create_random_graph()
    g.random_traversal()
    g.traverse_using_min_weight()
    g.traverse_using_prim()
    g.traverse_using_kruskal()