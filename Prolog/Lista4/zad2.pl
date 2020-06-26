istnieje(A, list(A, _, _, _, _)).
istnieje(A, list(_, A, _, _, _)).
istnieje(A, list(_, _, A, _, _)).
istnieje(A, list(_, _, _, A, _)).
istnieje(A, list(_, _, _, _, A)).

prawo(R, L, list(L, R, _, _, _)).
prawo(R, L, list(_, L, R, _, _)).
prawo(R, L, list(_, _, L, R, _)).
prawo(R, L, list(_, _, _, L, R)).

srodkowy(A, list(_, _, A, _, _)).

pierwszy(A, list(A, _, _, _, _)).

obok(A, B, list(B, A, _, _, _)).
obok(A, B, list(_, B, A, _, _)).
obok(A, B, list(_, _, B, A, _)).
obok(A, B, list(_, _, _, B, A)).
obok(A, B, list(A, B, _, _, _)).
obok(A, B, list(_, A, B, _, _)).
obok(A, B, list(_, _, A, B, _)).
obok(A, B, list(_, _, _, A, B)).
% kolor, pochodzenie, co pije, co pali, zwierze 
zagadka(Domy) :-
  pierwszy(dom(_,norweg, _, _, _),Domy),
  istnieje(dom(czerwony, anglik, _, _, _),Domy),
  prawo(dom(bialy,_,_,_,_), dom(zielony,_,_,_,_), Domy),
  istnieje(dom(_,dunczyk, hetbatka, _, _), Domy),
  obok(dom(_,_,_,papierosyLight,_), dom(_,_,_,_,koty), Domy),
  istnieje(dom(zolty, _,_,cygara,_),Domy),
  istnieje(dom(_,niemiec, _,fajka,_),Domy),
  srodkowy(dom(_,_,mleko,_,_),Domy),
  obok(dom(_,_,_,papierosyLight,_), dom(_,_,woda,_,_), Domy),
  istnieje(dom(_,_,_,papierosy, ptaki),Domy),
  istnieje(dom(_,szwed,_,_,psy),Domy),
  obok(dom(niebieski,_,_,_,_),dom(_,norweg,_,_,_),Domy),
  obok(dom(zolty,_,_,_,_),dom(_,_,_,_,konie),Domy),
  istnieje(dom(_,_,piwo,mentolowe,_),Domy),
  istnieje(dom(zielony,_,kawa,_,_),Domy),
  istnieje(dom(_,_,_,_,rybki),Domy).


rybki(X):-
    zagadka(Hs),
    istnieje(dom(_,X,_,_,rybki),Hs).