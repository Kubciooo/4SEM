Sposób użycia(po skompilowaniu programu): 
1)
./main --type quick|merge|insert|dualquick|radix --cmp '>='|'<=' 
następnie wpisujemy n
następnie n liczb do sortowania.

2)
./main --type quick|merge|insert|dualquick|insert-merge|radix --cmp '>='|'<=' --stat nazwa_pliku k
wyniki będą w pliku nazwa_pliku


jak widzimy na wykresach - dla danych a[i]<=2n radix sort radzi sobie lepiej zarówno od quicksorta, jak i mergesorta. Zmiana zakresu danych dla a[i] natomiast zwiększa liczbę operacji dla niego.  

