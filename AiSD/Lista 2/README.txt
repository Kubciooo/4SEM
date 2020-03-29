Sposób użycia: 
1)
./main --type quick|merge|insert|dualquick --cmp '>='|'<=' 
następnie wpisujemy n
następnie n liczb do sortowania.

Przykład użycia:
./main --type dualquick --cmp '>='
5
5 3 1 100 5

wyniki:
0.0000016930 sekund
porownania: 8, swapy: 7
100 5 5 3 1 


2)
./main --type quick|merge|insert|dualquick|insert-merge --cmp '>='|'<=' --stat nazwa_pliku k
wyniki będą w pliku nazwa_pliku


3) dla zadania 4
./main --type insert-merge --datatype string|int|float --MAX liczba(na jakim rozmiarze tablicy ma wchodzić insertsort) --cmp '<='|'>='|plik.txt (w plik.txt podajemy porządek)

Przykład użycia (z plikiem przyklad_porzadku.txt):
./main --type insert-merge --datatype float --MAX 4 --cmp przyklad_porzadku.txt
5
4.0 5.0 2.1 3.0 1.0

wyniki:
0.0000746760 sekund
porownania: 7, swapy: 4
5 4 2.1 3 1 



