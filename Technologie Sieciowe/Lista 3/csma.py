import random
from os import system, name 
import time

JAMMING_MESSAGE = "1001"

class PC():
    def __init__(self, username, dane, interval, polozenie):
        #nazwa użytkownika
        self.username = username
        #status 0 - słucha
        #status 1 - wysyła
        self.status = 0 
        #dane do wysłania
        self.dane = dane
        #co ile PC "chce" wysyłać dane
        self.interval = interval
        #położenie w sieci
        self.polozenie = polozenie
        #odległość do krańca sieci
        self.max_odleglosc = 0
        #jak długo nadaje sygnał 
        self.aktualny_czas_nadawania = 0
        #ile jeszcze będzie nasłuchiwał 
        self.pauza = interval
        #lista danych, które odebraliśmy 
        self.odebrane_dane = []
        #ostatni sygnał zawiera ostatnio otrzymaną informację 
        self.ostatni_sygnal = ''
        #ile już było kolizji na tym PC 
        self.R = 0



    def wykonaj_akcje(self, sygnaly):
        "zwracanie: 0 - słuchaj, 1 - wysyłaj, 2 - zgłoś kolizję"
        #jeżeli na naszym węźle jest tylko jeden sygnał, to chcemy go obsłużyć 
        if len(sygnaly) == 1:
            #jeżeli ten sygnał to JAMMING_MESSAGE, to nasz ostatni sygnał jest nieważny przez kolizję 
            if sygnaly[0].dane == JAMMING_MESSAGE:
                 self.ostatni_sygnal = ''
            #jeżeli otrzymamy inny sygnał od JAMMING MESSAGE i ostatni sygnał nie był pusty, to znaczy, że możemy odebrać ostatni sygnał
            elif sygnaly[0].dane != self.ostatni_sygnal and self.ostatni_sygnal != '':
                self.odebrane_dane.append(self.ostatni_sygnal)
                self.ostatni_sygnal = sygnaly[0].dane
            #jeżeli otrzymaliśmy nowe dane, a nasz ostatni sygnał był pusty, to nasz nowy ostatni sygnał to otrzymane dane 
            else:
                self.ostatni_sygnal = sygnaly[0].dane
        #jeżeli skończyliśmy otrzymywać sygnał, to jeżeli jakiś sygnał otrzymaliśmy, to dodajemy go do listy 
        elif len(sygnaly) == 0:
            if self.ostatni_sygnal != '':
                self.odebrane_dane.append(self.ostatni_sygnal)
                self.ostatni_sygnal = ''
        #jeżeli mamy kilka sygnałów naraz, to znaczy, że powstanie kolizja, więc nie bierzemy żadnego z nich
        else:
            self.ostatni_sygnal = ''
        
        #zmniejszamy o 1 pozostały czas nasłuchiwania 
        if self.pauza > 0 and self.status == 0:
            self.pauza -= 1
       
        #jeżeli nasłuchujemy i mamy pauzę, to nadal nasłuchujemy 
        if self.pauza > 0 and self.status == 0: 
            return 0

        #jeżeli nasłuchujemy i otrzymujemy jakiś sygnał, to nadal chcemy nasłuchiwać
        if self.status == 0 and len(sygnaly) > 0:
            return 0
        #w przeciwnym wypadku kończymy nasłuchiwać i zaczynamy wysyłać 
        if self.pauza == 0 and self.status == 0:
            self.status = 1 
            return 1 
        # jeżeli jesteśmy w trakcie wysyłania, to chcemy zobaczyć: 
        if self.status == 1 and len(sygnaly) == 0:
            self.aktualny_czas_nadawania += 1
            #1) Czy jesteśmy pewni, że nie było kolizji - jeżeli tak, to kończymy wysyłać nasze dane i wypisujemy sukces
            if self.aktualny_czas_nadawania == self.max_odleglosc * 2: 
                #print(self.username," rozesłał swoje dane!") 
                self.status = 0
                self.aktualny_czas_nadawania = 0
                self.pauza = self.interval
                self.R = 0
                return 0 
            else: 
            #2) Nie jesteśmy pewni, że nie było kolizji - dalej wysyłamy te dane 
                return 1
        #jeżeli jesteśmy w trakcie wysyłania danych i odbierzemy jakieś inne dane, to znaczy, że mamy kolizję  
        if self.status == 1 and len(sygnaly) > 0 and sygnaly[0] != JAMMING_MESSAGE: 
            self.status = 0 
            self.aktualny_czas_nadawania = 0
            self.R += 1
            return 2 



class Sygnal():
    "klasa symulująca pojedynczy sygnał w sieci"
    #status 1 - wysyłaj w lewo 
    #status 2 - wysyłaj w prawo 
    #dane - dane w sygnale 
    def __init__(self, status, dane):
        self.status = status
        self.dane = dane

class Network():
    "Klasa symulująca naszą sieć"
    def __init__(self, dlugosc, komputery):
        #sygnały to tablica tablic zawierająca informacje o napięciach na naszej sieci 
        self.sygnaly = [ [] for i in range(dlugosc) ]
        #komputery to nasi userzy, co nadają i odbierająsygnały
        self.komputery = komputery
        #długość sieci
        self.dlugosc = dlugosc
        #ile czasu minelo 
        self.czas = 0  
        #flaga mówiąca, czy powinniśmy zakończyć program
        self.zakoncz = False
        for pc in komputery:
            #ustawiamy maksymalną odległość dla każdego PC
            pc.max_odleglosc = max(pc.polozenie, abs(dlugosc-pc.polozenie))

    def wykonaj_akcje(self):
        self.czas += 1
        #przesuńmy wszystkie sygnały na tablicy
        sygnaly_temp = [ [] for i in range(self.dlugosc) ]
        for i in range(self.dlugosc):
            for sygnal in self.sygnaly[i]:
                if sygnal.status == 1 and i > 0: 
                    sygnaly_temp[i-1].append(sygnal)
                if sygnal.status == 2 and i+1 < self.dlugosc:
                    sygnaly_temp[i+1].append(sygnal)

        self.sygnaly = sygnaly_temp 
        # print(self.czas)
        # for i in range(len(self.sygnaly)):
        #     print('[', end='')
        #     for u in self.komputery:
        #         if u.polozenie == i: 
        #             print(u.username, ":", end=' ')
        #     for s in self.sygnaly[i]:
        #         print(s.dane, end=' ')
        #     print(']', end='')
        # print()
        # for u in self.komputery:
        #     print(u.username," : ", u.odebrane_dane[:min(len(u.odebrane_dane), 5)], " : ", u.ostatni_sygnal)
        # print("_"*100)
        #wykonajmy akcję dla każdego użytkownika 
        for user in self.komputery: 
            akcja = user.wykonaj_akcje(self.sygnaly[user.polozenie])
            #akcja = 0 -> słucha
            #akcja = 1 -> wysyła
            #akcja = 2 -> kolizja 
            if akcja == 1:
                self.sygnaly[user.polozenie].append(Sygnal(2, user.dane)) 
                self.sygnaly[user.polozenie].append(Sygnal(1, user.dane))  
            if akcja == 2: 
                # czekaj losową ilość czasu w danym zakresie 
                user.pauza = random.randint(1, (2**(min(user.R, 10))-1)*self.dlugosc)
                if user.R >= 15:
                    self.zakoncz = True
                self.sygnaly[user.polozenie].append(Sygnal(2, JAMMING_MESSAGE)) 
                self.sygnaly[user.polozenie].append(Sygnal(1, JAMMING_MESSAGE))  


def main():
    pc1 = PC("RYSIEK","R", 3, 0)
    pc2 = PC("BRAJAN", "B", 35, 10)
    pc3 = PC("MANIEK", "M", 23, 19)
    siec = Network(20,[pc1, pc2])
    while not siec.zakoncz: 
        #system('cls')
        siec.wykonaj_akcje()
        #time.sleep(1)
    print(siec.czas)
if __name__ == "__main__":
    main()