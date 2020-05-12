odpalanie: 
python main.py --type rbt/hmap/bst
jeżeli nie działa "python" proszę spróbować
python3 main.py --type rbt/bst/hmap

Następnie podajemy n i w kolejnych n linijkach podajemy dane wejściowe (jak na przykładzie) 

Przykład odpalenia programu:
python3 main.py --type rbt < dane/input.txt


UWAGA! Tutaj mamy porządkowanie leksykograficzne. Czyli A < a < B < b < .... < Z < z. 
############################################################################################################################

ZADANIE 1: 

############################################################################################################################
1) Obliczanie nt: 
W celu obliczenia nt, czyli najbardziej optymalnej wielkości tablicy w hmap wykonałem następujące kroki: 
I) Stworzyłem plik testerka.py, który posiada 2 funkcje: tworzenie dużego pliku testowego, na którym mogę przeprowadzić testy oraz funkcję szukającą najbardziej optymalnej liczby nt. 
W celu znalezienia nt stworzyłem plik, który zawiera: 
- 500 000 razy insert losowego słowa długości 5 
- 500 000 razy delete losowego słowa długości 5
Dla takich danych dla nt= {1,...,1000} szukałem takiego nt, dla którego czas wykonania programu będzie najkrótszy. 
Po godzinie program wypluł wynik - (2.0311987999999985, 47). Więc najbardziej optymalne nt wynosi 47.  
Wielkość tablicy m natomiast ustawiłem domyślnie na 1 000 000 - chciałem ustawiać ją w zależności od n, aczkolwiek przez funcję "load" nie da się stwierdzić ile danych będziemy insertować. Dlatego myślę, że 1 000 000 to najbardziej optymalna wielkość tablicy 

2) Średni czas dla każdej funkcji: 
2.1) stworzenie programu generator_plikow.py - zawiera on funkcję generuj_plik, która bierze 3 argumenty:
- inserty - ilość insertów w jednym obrocie
- searche - ilość findów w jednym obrocie 
- delety - ilosć deletów w jednym obrocie 
Funkcja ta printuje: 
i) "insert " + losowe słowo o długości 3 -> inserty razy
ii) "find " + losowe słowo o długości 3 -> searche razy
iii) "delete" + losowe słowo o długości 3 -> delety razy
iv) "insert " + losowe słowo o długości 3 -> inserty razy
v) "find " + losowe słowo o długości 3 -> searche razy
vi) "delete" + losowe słowo o długości 3 -> delety razy
Stworzyłem plik o danych: inserty = 100 000, searche = 100 000, delety = 100 000.
Stworzyłem program "testy_czasow.py", który bierze na input dane (tak, jak w treści zadania) i przy każdej operacji zlicza jej czas wykonania dla każdej struktury. Następnie zliczam średni czas insertowania, finda i delete dla każdej struktury. Średnie czasy prezentowały się nastepująco: 
Insert:
Średni czas hmap:  4.011694192886352e-06
Średni czas rbt:  4.26542067527771e-05
Średni czas bst:  8.471451997756958e-05
Find:
Średni czas hmap:  2.6124584674835205e-06
Średni czas rbt:  3.2285737991333008e-06
Średni czas bst:  3.631811022758484e-05
Delete:
Średni czas hmap:  3.222287893295288e-06
Średni czas rbt:  3.869874477386475e-05
Średni czas bst:  0.00010501591324806213
############################################################################################################################

ZADANIE 2: 

############################################################################################################################
W celu rozwiązania tego zadania stworzyłem nowy plik - "testy_porownan.py". Działa on w następujący sposób: 
1) wczytaj n tak jak w treści zadania 1 
2) insert string -> dodaj string do wszystkich struktur
3) find string -> znajdź string we wszystkich strukturach

Przykładowe odpalenie programu dla pliku p1.txt: 
python3 testy_porownan.py < dane/p1.txt 


Do wszystkich struktur dodałem możliwość zliczania ilości porównań podczas procedury "find". 
Dzięki temu mogłem przelecieć przez cały input i zliczyć minimalną, maksymalną oraz średnią liczbę porównań dla każdej ze struktur. Niestety bst jest zbyt wolne na wczytanie plików ze strony (python wywala błąd o maksymalnej rekurencji), dlatego stworzyłem 3 pliki, które biorą 50 000 pierwszych słów z każdego z nich i na tej podstawie obliczyłem wyniki. Konwersję plików zrobiłem za pomocą napisanego przeze mnie programu "konwersja.py" 

Dla pliku p1.txt (równocześnie 120k elementów zainsertowanych, 100k findów), którego używałem w poprzednim zadaniu wyniki prezentują się następująco:
Średnia ilość porównań hmap:  1.016355
Minimalna ilość porównań hmap:  0
Maksymalna ilość porównań hmap:  10
Średnia ilość porównań rbt:  12.587585
Minimalna ilość porównań rbt:  0
Maksymalna ilość porównań rbt:  19
Średnia ilość porównań bst:  63.09611
Minimalna ilość porównań bst:  1
Maksymalna ilość porównań bst:  147

Dla pliku lotr1.txt (zawiera on insert i find 50k pierwszych słów z lotr.txt) wyniki wyglądają następująco:
Średnia ilość porównań hmap:  0.38246
Minimalna ilość porównań hmap:  0
Maksymalna ilość porównań hmap:  18
Średnia ilość porównań rbt:  8.71566
Minimalna ilość porównań rbt:  0
Maksymalna ilość porównań rbt:  22
Średnia ilość porównań bst:  46.78402
Minimalna ilość porównań bst:  1
Maksymalna ilość porównań bst:  5823
 
Dla pliku kjb1.txt (zawiera on insert i find 50k pierwszych słów z kjb.txt) wyniki wyglądają następująco: 
Średnia ilość porównań hmap:  0.27314
Minimalna ilość porównań hmap:  0
Maksymalna ilość porównań hmap:  7
Średnia ilość porównań rbt:  7.94614
Minimalna ilość porównań rbt:  0
Maksymalna ilość porównań rbt:  22
Średnia ilość porównań bst:  68.33402
Minimalna ilość porównań bst:  1
Maksymalna ilość porównań bst:  2816

Dla pliku aspell1.txt (zawiera on insert i find 25k pierwszych słów z aspell_wordlist.txt) wyniki wyglądają następująco:
Średnia ilość porównań hmap:  1.01224
Minimalna ilość porównań hmap:  1
Maksymalna ilość porównań hmap:  3
Średnia ilość porównań rbt:  13.15908
Minimalna ilość porównań rbt:  0
Maksymalna ilość porównań rbt:  25
Średnia ilość porównań bst:  4338.06716
Minimalna ilość porównań bst:  1
Maksymalna ilość porównań bst:  15616

Jak widzimy - praktycznie w każdym z testów nasza maksymalna ilość porównań w hmap jest śmiesznie mała. Jest to wynikiem tego, że dzięki haszowaniu tak naprawdę nasza hmap posiada bardzo mało elementów w każdej z podtablic. Ma to znaczny wpływ na find, ponieważ często szukamy elementów, które są jedynymi elementami w hmapie. Natomiast nawet jeżeli hmapa posiada dużo elementów podtablicy, to wtedy załącza się tam find z drzewa czerwono-czarnego. 
Drzewo czerwono-czarne natomiast średnio wykonuje finda w O(log(n)) - maksymalnie widzimy 25 porównań w pliku, w którym mamy zawsze różne dane posortowane leksykograficzne - dzieje się to właśnie przez balansowanie(zawsze wysokość drzewa jest bardzo przybliżona do log(n)) i widzimy, że rzeczywiście znacznie usprawnia to zwykłe drzewo, na którym nie możemy nawet wczytać wszystkich danych, ponieważ spowoduje to stackoverflow(tutaj akurat winny jest python). Nawet na tych przykładowych danych (zwłaszcza aspell1.txt) widzimy, że wysokość drzewa wynosi prawie tyle, ile jest na nim elementów - daje nam to złożoność rzędu O(n) w najgorszych przypadkach!  
Wszędzie natomiast widzimy, że minimalna liczba porównań to 0 - szukamy wszystkich elementów, więc też i roota, co daje właśnie takie, a nie inne minimum.
