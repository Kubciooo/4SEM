operacja(W, Op1, Op2):- W = Op1 + Op2.
operacja(W, Op1, Op2):- W = Op1 - Op2.
operacja(W, Op1, Op2):- W = Op1 * Op2.
operacja(W, Op1, Op2):- W = Op1 / Op2, Op2 =\= 0.

buduj([X],X).
buduj(L, X):-
    append(L1, L2, L),
    \+length(L1, 0),
    \+length(L2, 0),
    buduj(L1, X1),
    buduj(L2, X2),
    operacja(X,X1,X2).
 
wyrazenie(L, S, W):-
    buduj(L, X),
    S is X,
    W = X.
% chcemy naszą listę N elementów dzielić na 2 listy: L1 i L2 i sprawdzamy, czy L1 operacja L2 da nam wynik. Schodzimy rekurencyjnie.