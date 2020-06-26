

% przykład uruchomienia: 
% phrase(ab(succ(0)),X).
% phrase(abc(N), X)
ab(Count) --> a(Count), b(Count).

abc(Count) --> a(Count), b(Count), c(Count).
 
a(0) --> [].
a(succ(Count)) --> [a], a(Count).
 
b(0) --> [].
b(succ(Count)) --> [b], b(Count).
 
c(0) --> [].
c(succ(Count)) --> [c], c(Count).


abfib(Count) --> a(Count), bfib(Count).

bfib(0) --> [].
bfib(succ(0)) --> [b].
bfib(succ(succ(Count))) --> bfib(succ(Count)), bfib(Count).
% bfib(Count+2) = bfib(count+1) + bfig(Count)



% L2 = L1 + L3
%Mamy appenda => append(L1,L3,L2)
%?- phrase(p([1,2,3,1]), X, [4,5,6]).
% X = [1, 2, 3, 1, 4, 5, 6].
p([]) --> [].
p([X|Xs]) --> [X], p(Xs).
