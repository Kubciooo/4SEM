regula(+,X,0,X).
regula(+,0,X,X).
regula(+,X,Y,X+Y).
regula(+,-X,X,0).
regula(+,X,X,2*X).
regula(+,X,Y,Z):- number(X), number(Y), Z is X+Y.
regula(-,X,0,X).
regula(-,X,X,0).
regula(-,X,Y,X-Y).
regula(-,X,Y,Z):- number(X), number(Y), Z is X-Y.


regula(*,_,0,0).
regula(*,0,X,0).
regula(*,1,X,X).
regula(*,X,1,X).
regula(*,X,Y,X*Y).
regula(*,X*Y,W,X*Z):- number(Y), number(W), Z is Y*W.
regula(*,X,Y,Z):- number(X), number(Y), Z is X*Y.

regula(/,0,_,0).
regula(/,0,X,0).
regula(/,X,X,1).
regula(/,X,Y,X/Y).
regula(/,X,Y,Z):- number(X), number(Y), Z is X/Y.
regula(/,X*Y, Y, X).
regula(/,X*Y, X, Y).

regula(+, X*Y, X*Z, X*C):- number(Y), number(Z), C is Z+Y.
regula(+, Y*X, Z*X, C*X):- number(Y), number(Z), C is Z+Y.
regula(+, Y*X, X, C*X):- number(Y), C is Y+1.
regula(+, X*Y, X, X*C):- number(Y), C is Y+1.
uprosc(E, E) :- atomic(E), !. %! oznacza, że jeżeli już znalazłem rozwiązanie, to nie wracam szukać kolejnego
uprosc(E, F) :- 
    E =..[Op, La, Ra], %tworzę sobie listę z E
    uprosc(La, X),     %uprawszczam sobie lewą stronę
    uprosc(Ra, Y),     %upraszczam sobie prawą stronę
    regula(Op, X, Y, F).   %wykonuję Lewa (działanie) Prawa