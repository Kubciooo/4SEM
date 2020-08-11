import collections
import codecs
from bitarray import bitarray
import zad1
import sys
import os

def bytes(filename):
    return os.stat(filename).st_size


def fib(n):
    if n == 0:
        return (0, 1)
    elif n == 1:
        return (1, 1)
    else: 
        a, b = fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')

    
def zakoduj_fibonacci(n):
    if n == 0: 
        return '11'
    wynik = dict()
    max_i = 0
    while n != 0: 
        i = 0
        while fib(i)[1] <= n:
            wynik[i] = 0
            i += 1
            max_i = max(max_i, i)
        wynik[i] = 1
        n -= fib(i)[0]
    wynik[max_i + 1] = 1
    return ''.join([str(x) for x in wynik.values()])
        
def odkoduj_fibonacci_liczba(zakodowane_slowo):
    wynik = 0
    for i in range(len(zakodowane_slowo)-1):
        if zakodowane_slowo[i] == '1' and zakodowane_slowo[i+1] == '1':
            return wynik + fib(i)[0]
        else:
            if zakodowane_slowo[i] == '1':
                wynik += fib(i)[0]

def podziel_finonacci(zakodowane_slowo, liczby = []):
    s = ''
    i = 0
    j = 0
    while i < len(zakodowane_slowo)-1:
        if zakodowane_slowo[i] == '1' and zakodowane_slowo[i+1] == '1':
            liczby.append(s+'11')
            i+=1
            s = ''
        else:
            s = s + zakodowane_slowo[i]
        i += 1
    return liczby
def odkoduj_fibonacci(zakodowane_slowo):
    liczby = podziel_finonacci(zakodowane_slowo)
    wynik = []
    for liczba in liczby:
        wynik.append(odkoduj_fibonacci_liczba(liczba))
    return wynik
        
def zakoduj_elias_gamma(n):
    reprezentacja_binarna = "{0:b}".format(n)
    return '0'*(len(reprezentacja_binarna)-1) +reprezentacja_binarna


def odkoduj_elias_gamma(zakodowane_slowo):
    i = 0
    wynik = []
    n = 0
    while i < len(zakodowane_slowo):
        if zakodowane_slowo[i] == '1':
            s = zakodowane_slowo[i:i+n+1]
            wynik.append(int(s,2))
            i += n+1
            n = 0
        else:
            n += 1
            i += 1
    return wynik

def zakoduj_elias_delta(n):
    reprezentacja_binarna = "{0:b}".format(n)
    L = len(reprezentacja_binarna)
    x1 = zakoduj_elias_gamma(L)
    return x1 + reprezentacja_binarna[1:]


def odkoduj_elias_delta(zakodowane_slowo):
    i = 0
    wynik = []
    L = 0
    while i < len(zakodowane_slowo):
        if zakodowane_slowo[i] == '1':
            s = zakodowane_slowo[i:i+L+1]
            N = int(s,2) - 1
            i += L+1
            s = zakodowane_slowo[i:i+N]
            i+= N
            wynik.append(pow(2,N) + int(s or '0',2))
            L = 0
        else:
            L += 1
            i += 1
    return wynik


def zakoduj_elias(n):
    wynik = "0"
    k = n
    while k > 1:
        reprezentacja_binarna = "{0:b}".format(k)
        wynik = reprezentacja_binarna + wynik
        k = len(reprezentacja_binarna)-1
    return wynik

def recursive_decode(s, n=1):
    if s[0]=="0":
        return [n, s[1:]]
    else:
        m = int(s[:n+1], 2)
        return recursive_decode(s[n+1:], m)


def odkoduj_eliasa(wynik):
    kodowanie = recursive_decode(wynik)
    kod = [kodowanie[0]]
    while kodowanie[1] != '':
        kodowanie = recursive_decode(kodowanie[1])
        kod.append(kodowanie[0])
    return kod



def zwroc_slowo(slownik, slowo):
    for klucz, ciag in slownik.items():
        if slowo == ciag:
            return klucz

def czy_w_slowniku(slownik, slowo):
    for ciag in slownik.values():
        if slowo == ciag:
            return True
    return False

def kodowanie_LZW(filename):
    with codecs.open(filename, "r", "utf-8", errors='ignore') as file:
        wejscie = file.read()
    znaki = list(dict(collections.Counter(wejscie)).keys())
    slownik = {i+1 : znaki[i] for i in range(len(znaki))}
    nastepny_indeks = len(znaki)+1
    wynik = []
    if not wejscie: 
        return
    c = wejscie[0]
    for s in wejscie[1:]:
        if czy_w_slowniku(slownik, c+s):
            c = c+s
        else: 
            wynik.append(zwroc_slowo(slownik,c))
            slownik[nastepny_indeks] = c+s
            nastepny_indeks +=1
            c = s
    wynik.append(zwroc_slowo(slownik,c))
    return wynik
        

def dekodowanie_LZW(ciag, slownik, fileout):
    wynik = ''
    f = codecs.open(fileout, "w", "utf-8", errors='ignore')
    poprzednie_slowo_kodu = ciag[0]
    wynik += slownik[poprzednie_slowo_kodu]
    nastepny_indeks = len(slownik)+1
    for slowo_kodu in ciag[1:]:
        poprzedni_ciag = slownik[poprzednie_slowo_kodu]
        if slowo_kodu in slownik.keys():
            slownik[nastepny_indeks] = poprzedni_ciag+slownik[slowo_kodu][0]
            wynik += slownik[slowo_kodu]
            nastepny_indeks += 1
        else:
            slownik[nastepny_indeks] = poprzedni_ciag+poprzedni_ciag[0]
            wynik += poprzedni_ciag + poprzedni_ciag[0]
            nastepny_indeks += 1
        poprzednie_slowo_kodu = slowo_kodu
    f.write(wynik)
         



filename = sys.argv[1]
filenamewyn = sys.argv[2]
wyn = open(filenamewyn, "wb")

a = kodowanie_LZW(filename)
wynik = ''
for znak in a:
    wynik = wynik + zakoduj_elias(znak)

d = bitarray(wynik)
d.tofile(wyn)
wyn.close()
print(a)
print()
file =  codecs.open(filename, "r","utf-8", errors='ignore')
wejscie = file.read()
znaki = list(dict(collections.Counter(wejscie)).keys())
slownik = {i+1 : znaki[i] for i in range(len(znaki))}
dekodowanie_LZW(odkoduj_eliasa(wynik), slownik,sys.argv[3])
x,Y = zad1.get_array(sys.argv[1])
print("entropia przed kodowaniem: ", zad1.entropy(x))
x,Y = zad1.get_array(sys.argv[2])
print(x)
print("entropia po kodowaniu: ", zad1.entropy(x))
print("Stopień kompresji: ", bytes(sys.argv[1]),' do ', bytes(sys.argv[2]))
