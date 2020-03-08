
divisible_h(X,Y):-
    (X mod Y) =:= 0.

divisible(X,Y):-
    divisible_h(X,Y);
    (X > Y+1, divisible(X,Y+1)).


prime(LO, HI, N):-
    between(LO, HI, N),
    N =\= 1,
    (\+ divisible(N,2); N =:= 2).