browse(Term) :-
	czytaj_polecenie(Term, [], []), !.

czytaj_polecenie(Term, Ojcowie, Synowie):- %Ojcowie to po kolei powrzucane wierzchołki, do ktorych weszlismy
    write(Term),                        %Pierwszy syn to poddrzewo aktualnego ojca
    write('\n Co robic?: '),
    read(C),
    wykonaj_polecenie(Term, Ojcowie, Synowie, C).


wykonaj_polecenie(Term, Ojcowie, Synowie, 'i'):-
    Term =.. [F, Wejscie|Reszta], %rozłóżmy term na F(Wejscie), Wszystko inne
    NowiOjcowie = [F|Ojcowie], % Dodajemy do listy Ojców nasze F 
    NowiSynowie = [[Wejscie|Reszta]|Synowie],  % Na poczatek listy synow dajemy listę synów F
    czytaj_polecenie(Wejscie, NowiOjcowie, NowiSynowie).  %Zwracamy pierwszego Syna F

wykonaj_polecenie(_, [], [], 'o'):- true. % nie mozemy wyjsc wyzej 
wykonaj_polecenie(_, [PierwszyOjciec|Ojcowie], [PierwszySyn|Synowie], 'o'):- 
    Term =.. [PierwszyOjciec|PierwszySyn],  % Usuwamy pierwszego ojca na liście i jego synów i ich wyświetlamy
    czytaj_polecenie(Term, Ojcowie, Synowie). 

wykonaj_polecenie(Term, Ojcowie, [PierwszySyn|Synowie], 'n'):-
    append(_,[Term, Brat|_], PierwszySyn), %Przechodzimy na prawego brata 
    czytaj_polecenie(Brat, Ojcowie, [PierwszySyn|Synowie]).

wykonaj_polecenie(Term, Ojcowie, [PierwszySyn|Synowie], 'p'):-
    append(_, [Brat, Term|_], PierwszySyn), %Przechodzimy na lewego brata 
    czytaj_polecenie(Brat, Ojcowie, [PierwszySyn|Synowie]).

wykonaj_polecenie(Term, Ojcowie, Synowie, _):-
    czytaj_polecenie(Term, Ojcowie, Synowie).




