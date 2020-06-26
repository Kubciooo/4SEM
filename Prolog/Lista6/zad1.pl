:- consult('scanner.pl'). 

program([]) --> [].
program([Instrukcja|PROGRAM]) -->
    instrukcja(Instrukcja), [sep(';')], program(PROGRAM).

 




instrukcja(assign(ID, Wyrazenie)) -->  
    [id(ID)], [sep(':=')], wyrazenie(Wyrazenie).
instrukcja(read(ID)) -->
    [key(read)], [id(ID)].
instrukcja(write(Wyrazenie)) -->
    [key(write)], wyrazenie(Wyrazenie).
instrukcja(if(Warunek, PROGRAM)) -->
    [key(if)], warunek(Warunek), [key(then)], program(PROGRAM), [key(fi)].
instrukcja(if(Warunek, PROGRAM_A, PROGRAM_B)) -->
    [key(if)], warunek(Warunek), [key(then)], program(PROGRAM_A), [key(else)], program(PROGRAM_B), [key(fi)].
instrukcja(while(Warunek, PROGRAM)) -->
    [key(while)], warunek(Warunek), [key(do)], program(PROGRAM), [key(od)].




wyrazenie(Skladnik + Wyrazenie) -->
    skladnik(Skladnik), [sep('+')], wyrazenie(Wyrazenie).
wyrazenie(Skladnik - Wyrazenie) -->
    skladnik(Skladnik), [sep('-')], wyrazenie(Wyrazenie).
wyrazenie(Skladnik) -->
    skladnik(Skladnik).


skladnik(Czynnik * Skladnik) -->
    czynnik(Czynnik), [sep('*')], skladnik(Skladnik).
skladnik(Czynnik / Skladnik) -->
    czynnik(Czynnik), [sep('/')], skladnik(Skladnik).
skladnik(Czynnik mod Skladnik) -->
    czynnik(Czynnik), [key(mod)], skladnik(Skladnik).
skladnik(Czynnik) -->
    czynnik(Czynnik).


czynnik(id(ID)) -->
    [id(ID)].
czynnik(int(NUM)) -->
    [int(NUM)].
czynnik((Wyrazenie)) -->
    [sep('(')], wyrazenie(Wyrazenie), [sep(')')].


warunek((Koniunkcja ; Warunek)) -->
    koniunkcja(Koniunkcja), [key(or)], warunek(Warunek).
warunek(Koniunkcja) -->
    koniunkcja(Koniunkcja).
koniunkcja((Prosty, Koniunkcja)) -->
    prosty(Prosty), [key(and)], koniunkcja(Koniunkcja).
koniunkcja(Prosty) -->
    prosty(Prosty).

    
prosty(Wyrazenie_A =:= Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('=')], wyrazenie(Wyrazenie_B).

prosty(Wyrazenie_A =\= Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('/=')], wyrazenie(Wyrazenie_B).

prosty(Wyrazenie_A < Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('<')], wyrazenie(Wyrazenie_B).

prosty(Wyrazenie_A > Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('>')], wyrazenie(Wyrazenie_B).

prosty(Wyrazenie_A >= Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('>=')], wyrazenie(Wyrazenie_B).

prosty(Wyrazenie_A =< Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('=<')], wyrazenie(Wyrazenie_B).

prosty(Wyrazenie_A < Wyrazenie_B) -->
    wyrazenie(Wyrazenie_A), [sep('<')], wyrazenie(Wyrazenie_B).

prosty((Wyrazenie)) -->
    [sep('(')], wyrazenie(Wyrazenie), [sep(')')].