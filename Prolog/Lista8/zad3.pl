:- use_module(library(clpfd)).

odcinek(Xs):-
    Xs = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16],
    Xs ins 0..1,
    sum(Xs,#=,8),
    chain([R1,R2,R3,R4,R5,R6,R7,R8],#=<),
    chain([R9,R10,R11,R12,R13,R14,R15,R16],#>=).
