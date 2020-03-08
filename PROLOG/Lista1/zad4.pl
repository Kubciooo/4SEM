le(a,a).
le(a,b).
le(a,c).
le(a,d).
le(a,e).

le(b,b).
le(b,c).
le(b,e).

le(c,c).
le(c,e).

le(d,d).
le(d,e).

le(e,e).


minimalny(X):- /* taki, który nie ma mniejszych od siebie */
    le(X,X), /*bo musi sam ze sobą być w relacji*/
    \+ (le(Y,X),X \= Y). /*nie ma mniejszego*/

maksymalny(X) :-
    le(X, X), 
    \+ (le(X, Y), X \= Y).

najmniejszy(X):- /*mniejszy od wszystkich elementów, czyli nie istnieje taki Y, który nie ma relacji z X i nie istnieje taki Y, który jest mniejszy od X */
    le(Y,Y),
    \+ (le(Y,Y), \+ le(X,Y)). 

najwiekszy(X) :-
	le(X, X), 
	\+ (le(Y, Y), \+ le(Y, X)).
    /* nieprawda, że jednocześnie jest jakiś Y(le(Y,Y)) w relacji, który nie jest mniejszy od X (\+ le(Y, X))