:- consult('zad1.pl').
:- consult('interpreter.pl').

wykonaj(Plik) :-
    open(Plik, read, X),
	scanner(X, Y),
	close(X),
    phrase(program(Program), Y),
	interpreter(Program).