arc(a, b).
arc(b, a).
arc(b, c).
arc(c, d).
arc(c, e).
arc(e, a). 
arc(d, e).

osiagalny(X, Y) :- osiagalny(X,Y,[]). %potrzebna nam lista odwiedzonych 

osiagalny(X, Y, _) :- arc(X,Y). %kiedy X i Y są połączone 
osiagalny(X, Y, V) :- \+ member(X, V), arc(X, Z), osiagalny(Z, Y, [X|V]). %kiedy z X jeszcze nie szliśmy(w tym wywołaniu chociażby)
% istnieje takie Z połączone z X, że istnieje droga z Z do Y z założeniem, że X już jest odwiedzone.