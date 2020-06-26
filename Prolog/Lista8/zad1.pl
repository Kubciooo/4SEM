:- use_module(library(clpfd)).

kolorowanie(Xs):-
    Xs = [R1,R2,R3,R4,R5,R6,R7,R8,R9],
    Xs ins 1..3,
    maplist(#\=(R1), [R2,R4,R5,R6]),
    maplist(#\=(R2), [R3,R4,R9]),
    maplist(#\=(R3),[R4,R5,R9]),
    maplist(#\=(R4),[R5]),
    maplist(#\=(R5),[R6,R7,R9]),
    maplist(#\=(R6),[R7,R8]),
    maplist(#\=(R7),[R8,R9]),
    maplist(#\=(R8),[R9]).