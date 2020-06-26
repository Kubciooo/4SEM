zadanie 1

wywołanie programu: 
python3 zad1.py
następnie wpisujemy liczbę M
następnie podajemy M operacji
ZŁOŻONOŚCI:
insert: 
insert dodaje element na koniec listy i wywołuje heapify - O(1) + heapify przechodzi za każdym razem na i // 2 -> O(logn)
Czyli insert jest O(logn)

empty: 
zwraca wielkość listy - O(1) 

top: 
zwraca pierwszy element na liście - O(1) 

pop:
zapisuje pierwszy element z tablicy, i wrzuca na jego miejsce ostatni. Dla niego robimy heapify -> znowu O(logn), bo idziemy na i*2. 
Czyli pop jest O(logn)

priority: 
przechodzi przez listę w poszukiwaniu x, dla każdego (x, y < p) robi heapify -> O(nlogn). Pojedynczo robi log(n) operacji dla jednego x.

zadanie 2
wywołanie programu: 
python3 zad2.py
następnie podajemy parametr n 
następnie podajemy parametr m 
nastepnie w kolejnych m linijkach podajemy parametry u,v,w

UWAGA - program pobiera krawędzie między wierzchołkami od 1 do n. Jeżeli dostanie wierzchołek 0, to nie zadziała!!!

zadanie 3
UWAGA - program pobiera krawędzie między wierzchołkami od 1 do n. Jeżeli dostanie wierzchołek 0, to nie zadziała!!!
wywołanie programu:
python3 zad3.py -p|k 
następnie podajemy parametr n 
następnie podajemy parametr m 
nastepnie w kolejnych m linijkach podajemy parametry u,v,w

zadanie 4
UWAGA - program pobiera krawędzie między wierzchołkami od 1 do n. Jeżeli dostanie wierzchołek 0, to nie zadziała!!!
wywołanie programu:
python3 zad4.py 
następnie podajemy n
następnie w kolejnych n(n-1)/2 linijkach podajemy parametry u,v,w

Za pomocą programu random_graph.py służącego do tworzenia losowego grafu pełnego spełniającego równanie trójkąta stworzyłem 4 pliki tekstowe: 5.txt, 50.txt, 500.txt, 5000.txt. Ten ostatni waży 184MB, więc nie został dodany do svna. Następnie przepuściłem program przez te wszystkie pliki. Wyniki odpowiednio w plikach out5.txt, out50.txt, out500.txt oraz out5000.txt. Dla Kruskala i Prima dodatkowo pierwsza linijka to suma wag mst zbudowanego przez te algorytmy.

W celu zbadania, czy wyniki dla Prima będą zawsze takie same, jak dla Kruskala po prostu dodałem do programu obie możliwości.
Czyli wykonujemy polecenie zarówno algorytmem Prima, jak i Kruskala. Jak można zauważyć - wyniki obu algorytmów są różne. Wynika to z tego, że nasz końcowy wynik jest zależny od wierzchołka startowego, a jako, że w obu algorytmach wybieram start losowo, to po prostu nawet jeżeli drzewa są takie same, to potem przy łączeniu kolejnych wierzchołków trochę inne wyniki się robią (bo zgodnie z algorytmem: przechodząc dfsem jeżeli któreś miasto pojawi się 2 razy, to łączymy jego poprzednika z sukcesorem).

TESTY:
Jak można się było spodziewać - losowe przechodzenie zajmuje najwięcej kroków i generuje największy koszt. Natomiast (czego się nie spodziewałem) średni czas jest dosyć niski w porównaniu do reszty algorytmów. Dzieje się to dlatego, że przejście do następnego wierzchołka zajmuje nam praktycznie zero czasu, gdzie przy pozostałych algorytmach mamy: 
- O(n) dla MINIMALNYCH WAG 
- O(1) dla Prima, ale trzeba zbudować jeszcze zbudować mst, co zajmuje O(|E|log|V|) 
- O(1) dla Kruskala, ale też trzeba zbudować jeszcze zbudować mst, co zajmuje O(|E|log|V|+|E|log|V|)

Przez potrzebę budowania drzewa w dwóch ostatnich podpunktach - ich czasy będą największe.
Jeżeli chodzi o liczbę kroków i koszt: 
Dla minimalnych wag zawsze mamy najmniej kroków - w każdym wierzchołku jesteśmy dokładnie raz, natomiast w Kruskalu i Prismie po 2 razy. 
Koszt jest tam również najmniejszy dla minimalnych wag. Natomiast widać, że dla prima i Kruskala mamy bardzo podobne wyniki, a na dodatek zgodnie z Algorytmem Christofidesa i Serdyukova mamy mniej więcej 1.5*optymalny_wynik. Jak można było się spodziewać - błądzenie losowe jest bardzo słabym rozwiązaniem. 
Z uwagi na to, że mój Kruskal tworzy graf inaczej, to dodatkowo dla niego muszę jeszcze tworzyć osobny graf, przez to jego czasy i pamięć są największe. 

W Primie i Kruskalu przechodzę po prostu dfsem wygenerowanie przez nie krawędzie. Robi on to w czasie liniowym od liczby krawędzi. 

Dodatkowo w trosce o swój komputer - nie próbowałem robić testów na większych zbiorach, bo już dla 10k elementów mój program zabierał 12GB RAMu.
