import os
import hashlib
import operator
import collections
import sys

def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()

def get_filenames(dir):
    dictionary = {}
    for root, dirs, files in os.walk(dir, topdown=False): 
        for f in files:
            dictionary[os.path.join(root,f)] = md5sum(os.path.join(root,f))
    
    return dictionary

if len(sys.argv) == 2:
    x = get_filenames(sys.argv[1]) #zwraca nam słownik nazwa_pliku : hash 


    sorted_x = sorted(x.items(), key=operator.itemgetter(0)) #sortujemy sobie po hashu
    sorted_dict = collections.OrderedDict(sorted_x) #posortowany słownik
    klucze = []
    wartosci = []
    for a in sorted_dict.keys():
        klucze.append(a)
        wartosci.append(sorted_dict[a]) #rozbijamy słownik na klucze i wartości 
    print("--"*50)
    if wartosci[0] == wartosci[1]:
        print(klucze[0] + " : " + wartosci[0])
    for i in range(1,len(klucze)): # po wartościach sprawdzamy, czy poprzednia lub następna jest taka sama i wtedy wypisujemy
        if wartosci[i] == wartosci[i-1] and i+1 != len(klucze) and wartosci[i] != wartosci[i+1]:
            print(klucze[i] + " : ",wartosci[i])
            print("--"*50)
        elif wartosci[i] == wartosci[i-1] and i+1 != len(klucze) and wartosci[i] ==wartosci[i+1]:
            print(klucze[i] + " : ",wartosci[i])
        elif i+1 != len(klucze) and wartosci[i] == wartosci[i+1]:
            print(klucze[i] + " : ",wartosci[i])
        elif wartosci[i] == wartosci[i-1] and i+1 == len(klucze):
            print(klucze[i] + " : ",wartosci[i])
else:
    print("Niepoprawny format wejściowy")