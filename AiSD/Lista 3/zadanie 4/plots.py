from matplotlib import pyplot as plt
import numpy as np

def get_data(filename):
    n = []
    time = []
    swaps = []
    comps = []
    memory = []
    with open(filename) as file:
        x = [l.strip() for l in file]
        for y in x:
            z = y.split(" ")
            n.append(int(z[0]))
            time.append(float(z[1]))
            swaps.append(int(z[2]))
            comps.append(int(z[3]))
            memory.append(int(z[4]))
    return n, time, swaps, comps, memory 

n, time, swaps, comps, memory = get_data("dual.txt")        
n2, time2, swaps2, comps2, memory2 = get_data("dualselect.txt")
#n3, time3, swaps3, comps3, memory3 = get_data("radix1000n.txt")

fig, ax = plt.subplots()
ax.plot(n,time ,label="dual pivot quicksort")
ax.plot(n2,time2,label="dual pivot quicksort z selectem")
#ax.plot(n3,swaps3,label="a[i] <= 1000n")

ax.set_title("Porównanie czasów od n")
ax.legend(loc="upper left")
plt.xlabel("n")
plt.ylabel("czas")
plt.show()