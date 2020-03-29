import random
import sys
import getopt
def nwd(a, b):
    """ funkcja pomocnicza, potrzebna do funkcji generuj_klucze"""
    while b != 0:
        a, b = b, a % b
    return a

def szybkie_potegowanie(liczba, potega, MOD=None):
    """ szybkie potęgowanie, żeby dużo sprawniej liczyć test millera rabina + generowanie dużych liczb"""
    wynik = 1
    while potega > 0:
        if potega % 2 == 1:
            wynik = (wynik * liczba)
            if MOD:
                wynik %= MOD
        potega = potega // 2 
        liczba = (liczba * liczba)
        if MOD:
            liczba %= MOD
    return wynik

def miller_rabin(p, s=5):
    """test na pierwszość liczby, p to nasz kandydat na liczbę pierwszą, a s to dokładność"""
    if p == 2:
        return True
    p1 = p - 1 # chcemy zapisać p-1 jako 2**u * r 
    u = 0       
    r = p1    # r = p1
    while r % 2 == 0: # tutaj szukamy największej potęgi dwójki, która dzieli p-1 
        r >>= 1
        u += 1

    assert p-1 == szybkie_potegowanie(2,u) * r  #sprawdzamy, czy p-1 == 2**u * d
    def świadek(a):   
        """ chcemy sprawdzić, czy liczba a podstawiona do wzoru: a**r mod p daje nam wynik 1 -> wtedy liczba a nie jest świadkiem, czyli """      
        z = szybkie_potegowanie(a, r, p) # z = a**r mod p 
        if z == 1:
            return False 
        # jeżeli ten wynik nie jest równy 1, to sprawdzamy, czy dla każdego i = 1,2,...,u-1: (z= (a **(2**i)*r) mod p), z != p1, bo jeżeli dla pewnego
        # i: z(i) == p-1, wtedy liczba może być pierwsza 
        for i in range(u):
            z = szybkie_potegowanie(a, szybkie_potegowanie(2,i) * r, p)
            if z == p1:
                return False 
        return True #liczba jest złożona 

    for j in range(s):# sprawdzamy pierwszość z dokładnością s
        a = random.randint(2, p-1)
        if świadek(a): #jeżeli jest jakiś świadek złożoności, to liczba nie jest złożona  
            return False 
    return True  

def generuj_pierwsza(k): 
    """funkcja generująca liczbę pierwszą do klucza k-bitowego"""
    k2 = k/2
    a = szybkie_potegowanie(2,k2)  
    a = int(a * (2**(-1/2)) + 1)
    b =szybkie_potegowanie(2,k-1)
    x = random.randint(a,b-2)
    if x % 2 == 0:
        x += 1
    while not miller_rabin(x): #dopóki x nie przejdzie testu pierwszości, to dodajemy 2 (OpenSSL tak robi)
        x += 2
    return x


def odwrotnosc_modulo(a, b):
    """ fukcja która wypisuje na wynik d, gdzie (a*d)%b = 1, https://eduinf.waw.pl/inf/alg/001_search/0009.php  """
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx

def generuj_klucze(bity):
    """ funkcja generująca klucze, bity = liczba bitów każdego klucza, https://pl.wikipedia.org/wiki/RSA_(kryptografia) """
    p = generuj_pierwsza(bity) 
    q = generuj_pierwsza(bity)
    while q == p:
        q = generuj_pierwsza(bity)
    n = p*q  
    phi = (p-1)*(q-1)
    e = random.randint(2,phi-1)
    while nwd(e, phi) != 1:
        e = random.randint(2, phi-1)
    d = odwrotnosc_modulo(e,phi)


    F1 = open("key.pub", "w")
    F2 = open("key.prv","w")
    F1.write(str(n)+ " "+str(e))
    F1.close()
    F2.write(str(n) + " "+str(d))
    F2.close()


def pobierz_klucze():
    """ funkcja pobierająca klucze z plików key.pub oraz key.prv """
    F1 = open("key.pub","r")
    F2 = open("key.prv","r")
    key_pub = F1.readline().split(" ")
    key_prv = F2.readline().split(" ")
    F1.close()
    F2.close()
    return key_pub, key_prv

def szyfruj(wiadomosc):
    """ funkcja szyfrująca wiadomość, https://pl.wikipedia.org/wiki/RSA_(kryptografia)"""
    klucze = pobierz_klucze()
    n1, e1 = klucze[0]
    n = int(n1)
    e = int(e1)
    wynik = -1 #tutaj będzie zaszyfrowana wiadomość
    if (len(wiadomosc) > 0):
        wynik = ord(wiadomosc[0])
    for i in range(1, len(wiadomosc)):
        wynik = wynik * 1000 + ord(wiadomosc[i]) # mnożymy przez tysiąc, ponieważ wszystko w ascii jest na max 3 cyfrach
    wynik = str((szybkie_potegowanie(wynik,e,n) % n))
    return wynik



def deszyfruj(wiadomosc):
    klucze = pobierz_klucze()
    n1, d1 = klucze[1]
    n = int(n1)
    d = int(d1)
    """ funkcja deszyfrująca wiadomość,  https://pl.wikipedia.org/wiki/RSA_(kryptografia)"""
    int_blocks = szybkie_potegowanie(int(wiadomosc),d,n) % n
    tmp = ""
    while int_blocks > 1000: #na każdym 1000 jest zapisany jeden char
        tmp = chr(int_blocks % 1000) + tmp
        int_blocks //= 1000
    tmp = chr(int_blocks % 1000) + tmp
    return tmp



def main(argv):
    try:
        opts, args = getopt.getopt(argv,"",["decode=", "encode=", "gen-keys="])
    except getopt.GetoptError:
        print("python rsa.py --decode <encoded_message> | --encode <message_to_encode> | --gen-keys <bit lenght>  ")
        sys.exit(2)
    [o, a] = opts[0] 
    if o == "--encode":
        print(szyfruj(a))
    elif o == "--decode":
        print(deszyfruj(a))
    else:
        generuj_klucze(int(a))
if __name__ == "__main__":
       main(sys.argv[1:])
