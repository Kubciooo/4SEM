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
    czas = []
    swapy = []
    porownania = []
    k = 1000
    with open(name+"1000.txt") as file:
        x = [l.strip() for l in file]
    for y in x: 
        z = y.split(',')
        #print(y)
        czas.append(float(z[1].split(" ")[2]))
        swapy.append(int(z[2].split(" ")[2]))
        porownania.append(int(z[3].split(" ")[2]))
    c = usrednij(k,swapy)
    p = usrednij(k,porownania)
    z = usrednij(k,czas)
    return z,c,p

n = [i for i in range(100,10000,100)]
n.append(10000)
fig, ax = plt.subplots()
k,c,p = plot("quick")
k2,c2,p2 = plot("dual")
p3 = []
for i in range(len(p)):
    sr = p[i] / p2[i]
    p3.append(sr)
print(max(p3))
ax.plot(n,k,label="quickSort")
ax.plot(n,k2,label="dualPivotQuickSort")
ax.set_title("Porównanie czasów w zależności od n dla k = 1000")
ax.legend(loc="upper left")
plt.show()

#