Sposób użycia(po skompilowaniu programu): 
1)
./main --type quick|merge|insert|dualquick|radix|quickselect|dualselect --cmp '>='|'<=' 
następnie wpisujemy n
następnie n liczb do sortowania.

2)
./main --type quick|merge|insert|dualquick|insert-merge|radix|quickselect|dualselect --cmp '>='|'<=' --stat nazwa_pliku k
wyniki będą w pliku nazwa_pliku


quicksort z selectem -> quickselect
dual pivot quicksort z selectem -> dualselect

Jak widzimy na wykresach - nasz select spowalnia programy nawet 4-krotnie. Prawdopodnie wynika to z tego, że dane są losowe i rzadko kiedy pojawia się najgorszy przypadek, na którym nasz select by uskutecznił programy. 