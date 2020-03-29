srodkowy(L, X) :-
    nieparzysta(L),
    same_length(Left, Right),
    append([Left, [X], Right], L), !.


nieparzysta([_]). %lista o rozmiarze 1 jest nieparzysta
nieparzysta([_|X]):- parzysta(X). %nieparzysta jest wtedy, kieddy lista o 1 mniejsza jest parzysta

parzysta([]). %lista o rozmiarze 0 jest parzysta
parzysta([_|X]):- nieparzysta(X).

same_length([], []). 
same_length([_|T1], [_|T2]) :- same_length(T1, T2). %tablice są równej długości, jeżeli tablice o 1 rozmiar mniejsze są równej długości
%czyli dla np. [1, 2, 3, 4, 5] mamy: 
% L1 = 1,2  R1 = 4,5 
