import numpy as np
import itertools
import functools 
import sys
def get_bytes_from_file(filename):  
    return open(filename, "rb").read()  




def get_column(arr, i):
    return [x[i] for x in arr]



def get_array(file):
    bytesArr =np.zeros((256,256), dtype=int) #tablica kwadratowa [x][y], zlicza ile razy po znaku y wystąpił znak x
    f = get_bytes_from_file(file)
    y = 0
    n =  []
    for x in f: 
        bytesArr[x][y] +=1 #po znaku y wystąpił znak x, dzięki temu możemy policzyć ile symboli wystąpiło po symbolu y oraz ile jest wystąpień znaku x
        y = x
        n.append(x) #plik przypisany na 8 bitową listę
    return n, bytesArr

##Entropy
def entropy(X):
    " wyliczanie entropii"
    value,counts = np.unique(X, return_counts=True) # usunięcie powtórzeń w x oraz zliczenie wszystkich wystąpień danego symbolu w X
    norm_counts = counts / counts.sum() #zliczanie prawdopodobieństwa wystąpienia symbolu
    return -(norm_counts * np.log(norm_counts)/np.log(2)).sum()


#Conditional Entropy
def conditional_entropy(Y): 
    suma = 0
    for i in range(256):
        for j in range(256):
            p = Y[j][i]
            if p > 0:
                p2 = np.sum(get_column(Y, i)) 
                suma += p * np.log2(p/p2)
    return -suma/np.sum(Y)


def entr(X):
    print(-np.sum([X[i]* np.log2(X[i]) for i in range(len(X))]))
def main():
    #x,Y = get_array(sys.argv[1])
    print("Entropia X: ",entropy(x))
    print("Entropia warunkowa Y|X: ",conditional_entropy(Y))



if __name__ == "__main__":
    entr([6/85, 8/85, 15/85, 5/85, 23/85, 6/85/ 7/85])
