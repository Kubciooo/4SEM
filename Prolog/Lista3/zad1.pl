sum([], 0). 
sum([X|L], N):-         %sumowanie tablicy
    sum(L, A), N is A+X. 


arithmetic(L, X):-          %średnia arytmetyczna
    sum(L, Suma),           %sumujemy tablicę
    length(L, N),           %wykorzystujemy predykat length/2 do zapisaniua rozmiaru tablicy do N 
    X is Suma/N.            % X to średnia arytmetyczna


wariancja(L, X):-       
    arithmetic(L, S),       %w S mamy średnią arytmetyczną
    arithmetic_var(L, A, S),% chcemy teraz zrobić licznik wariancji
    length(L, N),           %dzielimy licznik przez n
    X is A/N.           
    
arithmetic_var([], 0, _).       %dla listy bez elementów suma odchyleń to 0 
arithmetic_var([X|L], Y, Z):-       %Z -> nasza średnia arytmetyczna 
    arithmetic_var(L, Y2, Z),       % lecimy dalej   
    Y is Y2 + (X-Z)*(X-Z).          % I kolejny element sumy
    
