import numpy as np
import codecs
import sys
from bitarray import bitarray
import os
import zad1
def bytes(filename):
    return os.stat(filename).st_size


def zwroc_bity(lewy, prawy, licznik_Bitow, kod):
    while 1:
        if lewy >= 0 and prawy < 0.5:
            kod += '0'
            for i in range(licznik_Bitow):
                kod += '1'
            licznik_Bitow = 0
        elif lewy >= 0.5 and prawy < 1:
            kod += '1'
            for i in range(licznik_Bitow):
                kod += '0'
            licznik_Bitow = 0
            lewy -= (1)/(2)
            prawy -= (1)/(2)
        elif lewy >= 0.25 and prawy < 0.75:
            licznik_Bitow += 1
            lewy -= (1)/(4)
            prawy -= (1)/(4)
        else:
            break
        lewy *= (2)
        prawy *= (2)
    return lewy, prawy, licznik_Bitow, kod

def zakoncz_kodowanie_arytmetyczne(lewy, prawy, licznik_Bitow, kod):
    licznik_Bitow += 1
    if lewy < 0.25:
        kod += '0'
        for i in range(licznik_Bitow):
            kod += '1'
    else:
        kod += '1'
        for i in range(licznik_Bitow):
            kod += '0'
    return kod


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')


def kodowanie_arytmetyczne(plik):
    slownik = [ 1 for i in range(257)]
    liczba_slow = 257
    lewy = 0
    prawy = 1
    licznik_Bitow = 0
    kod = ''
    outfile = open(sys.argv[2],"wb")

    with open(plik, "rb") as file:
        komunikat = file.read() 
        for slowo in komunikat:
            lewy, prawy = lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo]))/ (liczba_slow))  , lewy + ( (prawy - lewy) * (sum(slownik[:slowo+1]))/(liczba_slow) )

            lewy, prawy, licznik_Bitow, kod = zwroc_bity(lewy, prawy, licznik_Bitow, kod)
            slownik[slowo] += 1
            liczba_slow +=1
        slowo = 256
        lewy, prawy = lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo]))/ (liczba_slow))  , lewy + ( (prawy - lewy) * (sum(slownik[:slowo+1]))/(liczba_slow) )

        lewy, prawy, licznik_Bitow, kod = zwroc_bity(lewy, prawy, licznik_Bitow, kod)
        slownik[slowo] += 1
        liczba_slow +=1

    kod =  zakoncz_kodowanie_arytmetyczne(lewy, prawy, licznik_Bitow, kod)
    d = bitarray(kod)
    d.tofile(outfile)

    return kod

def bin_to_float(bin_code):
    result = (0)
    act = 0.5
    for i, c in enumerate(bin_code, 1):
        result += (int(c))*(act)
        act /= 2

    return result

def odejmij_4(binarna):
    if binarna[1] == '1':
        binarna = binarna[:1]+'0'+binarna[2:]
    elif binarna[0] == '1':
        binarna = '01' + binarna[2:]
    return binarna



def odejmij_2(binarna):
    binarna = '0'+binarna[1:]
    return binarna


# def aktualizuj_liczbe_buforowa(lewy, prawy, slownik, liczba_slow):
#     najmniejszy = 1
#     x1 = 0
#     x2 = 1
#     for slowo in range(len(slownik)):
#         x1 = lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo])) / (liczba_slow))
#         x2 = lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo+1]))  / (liczba_slow))
#         if x2 - x1 < najmniejszy: 
#             najmniejszy = x2 - x1
#         k = np.log2(4/najmniejszy)
#     return k
def zwroc_litere(lewy, prawy, bufor_bitow, slownik, liczba_slow, zakodowane_slowo, aktualny_koniec_slowa, slowo):
    def zwroc():
        print("szukam słowa!")
        bt = bin_to_float(bufor_bitow)
        for slowo in range(len(slownik)):
            if lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo])) / (liczba_slow)) <= bt and bt < lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo+1]))  / (liczba_slow)):
                return slowo, lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo])) / (liczba_slow)), lewy + ( ( prawy - lewy ) * (sum(slownik[:slowo+1]))  / (liczba_slow))
    slowo, lewy, prawy  = zwroc()
    print("znalazłem słowo! Wchodzę do pętli!")
    while 1:
        if lewy >= 0 and prawy < 0.5:
            nic_nie_rob = 1
        elif lewy >= 0.5 and prawy < 1:
            bufor_bitow = odejmij_2(bufor_bitow)
            lewy -= (1)/(2)
            prawy -= (1)/(2)
        elif lewy >= 0.25 and prawy < 0.75:
            bufor_bitow = odejmij_4(bufor_bitow)
            lewy -= (1)/(4)
            prawy -= (1)/(4)
        else:
            break
        lewy *= (2)
        prawy *= (2)
        aktualny_koniec_slowa += 1
        if aktualny_koniec_slowa < len(zakodowane_slowo):
            bufor_bitow = bufor_bitow[1:]+zakodowane_slowo[aktualny_koniec_slowa]
        else: bufor_bitow = bufor_bitow[1:]
    print("Wyszedłem z petli!")
    return lewy, prawy, aktualny_koniec_slowa, bufor_bitow, slowo

def odkoduj(zakodowane_slowo, wyjscie):
    slownik = [1 for i in range(257)]
    outfile = open(wyjscie, "wb")
    liczba_slow = 257
    lewy = 0
    prawy = 1
    liczba_buforowa = 60
    aktualny_koniec_slowa = liczba_buforowa-1
    bufor_bitow = zakodowane_slowo[0:liczba_buforowa]
    slowo = 0
    odkodowana_wiadomosc = ''
    lewy, prawy, aktualny_koniec_slowa, bufor_bitow, slowo = zwroc_litere(lewy, prawy, bufor_bitow, slownik, liczba_slow, zakodowane_slowo,aktualny_koniec_slowa,slowo )
    s2 = "{0:b}".format(slowo)
    while len(s2) < 8:
        s2 = '0'+s2
    d = bitarray(s2)
    d.tofile(outfile)
    slownik[slowo] += 1
    liczba_slow += 1
    while slowo != 256:
        print("zaczynam zwracac litere!")
        lewy, prawy, aktualny_koniec_slowa, bufor_bitow, slowo = zwroc_litere(lewy, prawy, bufor_bitow, slownik, liczba_slow, zakodowane_slowo,aktualny_koniec_slowa,slowo )
        ("zwróciłem literę!")
        s2 = "{0:b}".format(slowo)
        while len(s2) < 8:
            s2 = '0'+s2
        if slowo != 256:  
            d = bitarray(s2)
            d.tofile(outfile)
        slownik[slowo] += 1
        liczba_slow += 1
        print(slowo)
x,Y = zad1.get_array(sys.argv[1])
print("entropia przed kodowaniem: ", zad1.entropy(x))
a = kodowanie_arytmetyczne(sys.argv[1])
x,Y = zad1.get_array(sys.argv[2])
print("entropia po kodowaniu: ", zad1.entropy(x))
print("Stopień kompresji: ", bytes(sys.argv[1])," do ",bytes(sys.argv[2])*100,'%')
#odkoduj(a, "odkodowanie.txt")
