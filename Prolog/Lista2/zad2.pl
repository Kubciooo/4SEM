jednokrotnie(X, L) :-           
    select(X, L, R),    % R = L\X 
    \+ member(X, R).    % X nie ma w R

dwukrotnie(X, L):-      
    select(X, L, R), % R = L/X 
    jednokrotnie(X, R).  %X występuje raz w R