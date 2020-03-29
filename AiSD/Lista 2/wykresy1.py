from matplotlib import pyplot as plt
import numpy as np

def dziel(tablica):
    j = 100
    for i in range(len(tablica)):
        tablica[i] = tablica[i] / j
        j += 100
    return tablica
def usrednij(k, tablica):
    wynikowa = []
    j = -1
    for i in range(len(tablica)):
        if i % k == 0:
            wynikowa.append(0)
            j+=1
        wynikowa[j] += tablica[i]
    for i in range(len(wynikowa)):
        wynikowa[i] = wynikowa[i]/k
    return wynikowa

def plot(name):
    x = []
    n = []
    czas = []
    swapy = []
    porownania = []
    k = 1
    with open(name+"1.txt") as file:
        x = [l.strip() for l in file]
    for y in x: 
        z = y.split(',')
        #print(y)
        n.append(int(z[0].split(" ")[1]))
        czas.append(float(z[1].split(" ")[2]))
        swapy.append(int(z[2].split(" ")[2]))
        porownania.append(int(z[3].split(" ")[2]))
    k1 = usrednij(k,swapy)
    c1 = usrednij(k,czas);
    p1 = usrednij(k,porownania);
    x = []
    czas = []
    swapy = []
    porownania = []
    k = 10
    with open(name+"10.txt") as file:
        x = [l.strip() for l in file]
    for y in x: 
        z = y.split(',')
        #print(y)
        czas.append(float(z[1].split(" ")[2]))
        swapy.append(int(z[2].split(" ")[2]))
        porownania.append(int(z[3].split(" ")[2]))
    k10 = usrednij(k,swapy)
    c10 = usrednij(k,czas);
    p10 = usrednij(k,porownania);

    x = []
    czas = []
    swapy = []
    porownania = []
    k = 100
    with open(name+"100.txt") as file:
        x = [l.strip() for l in file]
    for y in x: 
        z = y.split(',')
        #print(y)
        czas.append(float(z[1].split(" ")[2]))
        swapy.append(int(z[2].split(" ")[2]))
        porownania.append(int(z[3].split(" ")[2]))
    k100 = usrednij(k,swapy)
    c100 = usrednij(k,czas);
    p100 = usrednij(k,porownania);
    #plt.style.use('ggplot')
    # Fixing random state for reproducibility
    #fig, ax = plt.subplots()
    
    #ax.plot(n,czas,label="czas")
   # ax.plot(n, c1,label="k = 1")
   # ax.plot(n, c10,label="k = 10")
   # ax.plot(n, c100,label="k = 100")

  #  ax.set_title(name+"Sort: czas w zależności od n")
  #  ax.legend(loc="upper left")
    #plt.show()
    return k100,c100,p100
i1, i2, i3 = plot("insert") #1 -> przestawienia, 2-> czasy, 3->porównania
m1, m2, m3 = plot("merge")
q1, q2, q3 = plot("quick")
n = [i for i in range(100,10000,100)]
n.append(10000)
fig, ax = plt.subplots()
ax.plot(n,m3,label="mergeSort")
ax.plot(n,q3,label="quickSort")
ax.set_title("Porównanie ilości porównań w zależności od n")
ax.legend(loc="upper left")
plt.show()