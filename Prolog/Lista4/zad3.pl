kwadrat(male(9),L):-
    numlist(1, 24, L).

kwadrat(srednie(4), L):-
    kwadrat(male(9),L).

kwadrat(duze(1), [1, 2, 3, 4, 7, 11, 14, 18, 21, 22, 23, 24]).

kwadrat(male(1),[N1,N2,N3,N4]):-
    (
        between(1, 3, N1);
        between(8, 10, N1);
        between(15, 17, N1)  
    ),
    N2 is N1 + 3,
    N3 is N1 + 4,
    N4 is N1 + 7.

kwadrat(male(N),L):-
    between(2, 8, N),
    N2 is N - 1,
    kwadrat(male(N2), L2),
    kwadrat(male(1), L3),
    [Min1|_] = L2,
    [Min2|_] = L3,
    Min2 > Min1,
    intersection(L2, L3, L23),
    L3 \= L23,
    union(L2,L3,L4),
    sort(L4,L).


 kwadrat(srednie(1),[N1,N2,N3,N4,N5,N6,N7,N8]):-
    (
        between(1,2,N1);
        between(8,9, N1)
    ),
    N2 is N1 + 1,
    N3 is N1 + 3,
    N4 is N1 + 5,
    N5 is N1 + 10,
    N6 is N1 + 12,
    N7 is N1 + 14,
    N8 is N1 + 15.

kwadrat(srednie(N),L):-
    between(2,3, N),
    N2 is N - 1,
    kwadrat(srednie(N2),L2),
    kwadrat(srednie(1),L3),
  [Min1|_] = L2,
    [Min2|_] = L3,

    Min2 > Min1,
    intersection(L2, L3, L23),
    L3 \= L23,
    union(L2,L3,L4),
    sort(L4,L).

licz_kwadraty(male([]),X,X).
licz_kwadraty(male([N1|L]), W,Wyn):-
    (
        (
            (
                between(1, 3, N1);
                between(8, 10, N1);
                between(15, 17, N1)  
            ),
            N2 is N1 + 3,
            N3 is N1 + 4,
            N4 is N1 + 7,
            member(N2, L),
            member(N3, L),
            member(N4, L),
            W2 is W + 1
        ) ->  licz_kwadraty(male(L),W2,Wyn) ; licz_kwadraty(male(L), W,Wyn)
    ).

licz_kwadraty(srednie([]), X, X).
licz_kwadraty(srednie([N1|L]), W,Wyn):-
    (
        (
            (
                between(1,2,N1);
                between(8,9, N1) 
            ),
            N2 is N1 + 1,
            N3 is N1 + 3,
            N4 is N1 + 5,
            N5 is N1 + 10,
            N6 is N1 + 12,
            N7 is N1 + 14,
            N8 is N1 + 15,
            member(N2, L),
            member(N3, L),
            member(N4, L),
            member(N5, L),
            member(N6, L),
            member(N7, L),
            member(N8, L),
            W2 is W + 1
        ) ->  licz_kwadraty(srednie(L),W2,Wyn) ; licz_kwadraty(srednie(L), W,Wyn)
    ).

licz_kwadraty(duze(L), Wyn):-
(
    kwadrat(duze(1), L2),
    intersection(L, L2, L3),
    L2 \= L3 -> Wyn is 0 ; Wyn is 1 
).


zapalki(Z, (duze(N1), srednie(N2))) :-
	zapalki(Z, (duze(N1), srednie(N2), male(0))).
zapalki(Z, (duze(N1), male(N3))) :-
	zapalki(Z, (duze(N1), srednie(0), male(N3))).
zapalki(Z, (srednie(N2), male(N3))) :-
	zapalki(Z, (duze(0), srednie(N2), male(N3))).
zapalki(Z, (duze(N1))):-
    zapalki(Z,(duze(N1),srednie(0),male(0))).
zapalki(Z, (male(N1))):-
    zapalki(Z, (duze(0),srednie(0),male(N1))).
zapalki(Z,(srednie(N1))):-
    zapalki(Z,(duze(0),srednie(N1),male(0))).

kwadrat(duze(0),[]).
kwadrat(male(0),[]).
kwadrat(srednie(0),[]).


zapalki(N, (duze(Z),srednie(Y),male(X))):-
    kwadrat(srednie(Y),L1),
    kwadrat(male(X), L2),
    kwadrat(duze(Z), L3), 
    union(L1,L2,L4),
    union(L3,L4,L5),
    sort(L5,L),
    licz_kwadraty(male(L),0,X),
    licz_kwadraty(srednie(L),0,Y),
    licz_kwadraty(duze(L),Z),
    length(L, I),
    N is 24-I,
    narysuj_pole(L).
    

narysuj_zapalke(X) :-
	member(X, [2, 3, 9, 10, 16, 17, 23, 24]),
	write('---+').
narysuj_zapalke(X) :-
	member(X, [1, 8, 15, 22]),
	write('\n+---+').
narysuj_zapalke(X) :-
	member(X, [4, 11, 18]),
	write('\n|   ').
narysuj_zapalke(X) :-
	member(X, [5, 6, 7, 12, 13, 14, 19, 20, 21]),
	write('|   ').

narysuj_puste(X) :-
	member(X, [2, 3, 9, 10, 16, 17, 23, 24]),
	write('   +').
narysuj_puste(X) :-
	member(X, [1, 8, 15, 22]),
	write('\n+   +').
narysuj_puste(X) :-
	member(X, [4, 11, 18]),
	write('\n    ').
narysuj_puste(X) :-
	member(X, [5, 6, 7, 12, 13, 14, 19, 20, 21]),
	write('    ').

narysuj_pole(25, _) :-
	write('\n\n').
narysuj_pole(X, L) :-
(
	member(X, L) -> narysuj_zapalke(X) ; narysuj_puste(X)
),	
	X1 is X+1,
	narysuj_pole(X1, L).

narysuj_pole(L) :-
	narysuj_pole(1, L).