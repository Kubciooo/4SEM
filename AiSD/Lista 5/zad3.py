import kruskal
import prim
import sys 



def main():
    if len(sys.argv) != 2: 
        print("python main.py -p|k\n")
    else: 
        if sys.argv[1] not in ["-p","-k"]:
            print("python main.py -p|k")
        else: 
            n = int(input())
            m = int(input())
            if sys.argv[1] == "-p":
                g = prim.Graph(n)
            else:
                g = kruskal.Graph(n)
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
            


if __name__ == '__main__':
    main()

