niepoprawna(L):-
    member(X,L),
    length(L, DlugoscListy),
    X > DlugoscListy. 
    

zamien(L, Wyn):- % przez niedoczytanie program wypisywania tablicy działa w ten sposób, że nasza lista L składa się z pozycji 'i' od górnego lewego rogu i nioe zeruje się na kolejnym wierszu
    length(L, LiczbaHetmanow),
    zamien(L, [], Wyn, 1, LiczbaHetmanow).

zamien([], Term, Term, _, _):- !. 
zamien([Wiersz|L], Term, Wyn, Kolumna, DlugoscListy):- %funkcja ta zamienia nam dane wejsciowe na dane, ktore przyjmuje moj program 
    Z is ( DlugoscListy - Wiersz) * DlugoscListy + Kolumna,
    NastepnaKolumna is Kolumna + 1,
    zamien(L, [Z|Term], Wyn, NastepnaKolumna, DlugoscListy).

board(L):- % jezeli ktoras z liczb jest wieksza od wielkosci tablicy, to nie mozna odpalic programu
    niepoprawna(L),
    write('co najmniej jeden hetman jest na za dalekiej pozycji!\n'), !.


board(L):-
    zamien(L, Wyn), 
    \+niepoprawna(L), 
    length(Wyn, LiczbaHetmanow), 
    K is LiczbaHetmanow mod 2, % dla K = 0 zaczynamy od bialych 
    rysuj(1, Wyn, LiczbaHetmanow, K), !. 

    

rysuj(Wiersz, _, DlugoscListyHetmanow, _):-  % rysowanie ostatniego brzegu 
    Wiersz is DlugoscListyHetmanow + 1,
    rysuj_brzeg(DlugoscListyHetmanow, 0), !. 

rysuj(Wiersz, ListaHetmanow, DlugoscListyHetmanow, Bialy):- 
    rysuj_brzeg(DlugoscListyHetmanow, 0), %rysuj '+----+---+.....---+'
    Nastepny is Wiersz + 1, 
    Czarny is (Bialy + 1) mod 2,
    I is (Wiersz - 1) * DlugoscListyHetmanow + 1, %aktualna pozycja na której zaczyna sie aktualne pole 
    rysuj_pole(Bialy,ListaHetmanow, DlugoscListyHetmanow, I), % rysuj pole biale albo czarne 
    rysuj_pole(Bialy,ListaHetmanow, DlugoscListyHetmanow, I), % to samo drugi raz
    rysuj(Nastepny, ListaHetmanow, DlugoscListyHetmanow, Czarny). % kolejy wiersz 



     
rysuj_brzeg(Dlugosc, Dlugosc):-
    write('+\n'), !.
rysuj_brzeg(Dlugosc, Aktualny):-
    write('+-----'),
    Nastepny is Aktualny + 1,
    rysuj_brzeg(Dlugosc, Nastepny).



rysuj_pole(0, ListaHetmanow, DlugoscListyHetmanow, I):- %rysuj pole biale 
    write('|'),
    (
        (
            member(I, ListaHetmanow), % mamy na liscie hetmanow nasze I, wiec rysujemy tutaj hetmana 
            write(' ### ')
        );
        (
            \+member(I, ListaHetmanow),
            write('     ')
        )
    ),
    (
        (
            K is I mod DlugoscListyHetmanow,
            K \= 0,
            I2 is I+1,
            rysuj_pole(1, ListaHetmanow, DlugoscListyHetmanow, I2) % rysujemy czarne pole 
        );
        (
            K is I mod DlugoscListyHetmanow, 
            K = 0, % to bylo ostatnie pole do narysowania w tym wierszu 
            write('|\n'), !
        )
    ).

rysuj_pole(1, ListaHetmanow, DlugoscListyHetmanow, I):- %rysuj pole czarne 
    write('|'),
    (
        (
            member(I, ListaHetmanow), 
            write(':###:')
        );
        (
            \+member(I, ListaHetmanow),
            write(':::::')
        )
    ),
    (
        (
            K is I mod DlugoscListyHetmanow,
            K \= 0,
            I2 is I+1,
            rysuj_pole(0, ListaHetmanow, DlugoscListyHetmanow, I2)
        );
        (
            K is I mod DlugoscListyHetmanow,
            K = 0,
            write('|\n'), !
        )
    ).


    
% Tutaj mamy hetmany z wykladu 
perm([], []).
perm(L1, [X | L3]) :-
	select(X, L1, L2),
	perm(L2, L3).

dobra(X) :-
	\+ zla(X).

zla(X) :-
	append(_, [Wi | L1], X),
	append(L2, [Wj | _], L1),
	length(L2, K),
	abs(Wi - Wj) =:= K+1.

hetmany(N, P) :-
	numlist(1, N, L),
	perm(L, P),
	dobra(P).