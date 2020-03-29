max_sum(L, X):-
    max_sum(L,0,0,X).



max_sum([X|L], Aktualna, Najlepsza, Wynik):-
    Aktualna2 is max(Aktualna + X, 0),     % nie chcemy zejść poniżej 0, bo możemy zwracać 0 jako sumę 
    Najlepsza2 is max(Aktualna2, Najlepsza), % chcemy mieć zawsze najlepszą sumę jaka była do tej pory zapisana 
    max_sum(L, Aktualna2, Najlepsza2, Wynik). %i idziemy dalej 

max_sum([], _, Najlepsza, Najlepsza). %jak już przeszliśmy całą listę, to chcemy wynik zapisać do X 


