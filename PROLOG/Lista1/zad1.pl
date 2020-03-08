rodzic(asia,asiek).
rodzic(antek,asiek).
rodzic(asia,nana).
rodzic(rysiek, asia).
kobieta(nana).
kobieta(asia).
kobieta(ania).
jest_matka(X):-rodzic(X,Y),kobieta(X).
jest_ojcem(X):-rodzic(X,Y),\+kobieta(X).
jest_synem(X):-rodzic(Y,X),\+kobieta(X).
siostra(X,Y):-kobieta(X),rodzic(Z,X),rodzic(Z,Y),X\=Y.
dziadek(X,Y):-rodzic(X,Z),jest_ojcem(X),rodzic(Z,Y).
rodzenstwo(X,Y):-rodzic(Z,X),rodzic(Z,Y),X\=Y.