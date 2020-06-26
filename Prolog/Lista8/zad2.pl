:- use_module(library(clpfd)).
 
plecak(Ls,Ws,W,R) :-
        length(Ls, N),
        length(R, N),
        R ins 0..1,
        scalar_product(Ws, R, #=<, W),
        scalar_product(Ls, R, #=, VM),
        once(labeling([max(VM)], R)).