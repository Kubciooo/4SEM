lista(N,X) :- numlist(1, N, A), numlist(1, N, B), tworz(X,A,B).


tworz(L, [], []) :- L = [].

tworz(X, [Y|A], B):-  %[Y|A], bo chcemy, żeby z A szły po kolei nasze n(patrz: Uwaga 0)
    select(Z, B, B2), %B2 = B - Z, czyli bierzemy sobie jakiś element z B. 
    X = [Y, Z|X1],    % X = Y + Z + X1 => X1 = X - Y - Z, element z B jest też w X
    tworz(X1,A,B2).   %tworz(X-A-Z, Y, B-Z) 

%wersja ze wszystkimi możliwościami (czyli np. X = [3,2,1,3,2,1] też):
%    tworz(X,A,B):-
%        select(Z,B,B2),
%        select(Y,A,A2),
%        X = [Y, Z|X1],
%        tworz(X1,A2,B2).

%działanie twórz: chcemy otrzymać X, X na jakimś poziome to: X = Y(gdzie Y to pojedynczy element z A)
% + Z(też pojedynczy element ,tylko z B) _+ X1(gdzie X1 to jest X z poziomu niżej)
% czyli dla lista(3, X) mamy przykładowo: 
% tworz(X, [1,2,3], [1,2,3]):
% Z = 1, Y = 1
% X = [1,1, X1]
% tworz(X1, [2,3], [2,3])
% 

%dlaczego to działa? Bo nasza lista wygląda tak: a należy do A, b należy do b : abababababab... w A i w B każde n jest tylko raz.
% czyli nie ma szans, że istnieje jakaś liczba w tym ciągu, która jest od drugiej siebie w odległości nieparzystej, bo to by znaczyło,
% że jedna liczba występuje 2 razy w A lub B. 


