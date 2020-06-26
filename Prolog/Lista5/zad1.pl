key(read).
key(write).
key(if).
key(then).
key(else).
key(fi).
key(while).
key(do).
key(od).
key(and).
key(or).
key(mod).
white(' ').
white('\n').
white('\t').
sep(;).
sep(:).
sep(+).
sep(-).
sep(*).
sep(/).
sep('(').
sep('[').
sep(']').
sep(')').
sep(>).
sep(<).
sep(=).
sep(<=).
sep(>=).
sep(/=).
sep(:=).
id_token(Token, id(Token)).
int(Character):-
    atom_number(Character, Number),
    integer(Number),
    Number >= 0.

id(Character):-
    char_type(Character, upper).

key_candidate(Character):-
    char_type(Character,lower).

scanner(Strumien, Tokeny):-
    current_input(Curr),
    set_input(Strumien),
    scan(Tokeny),
    set_input(Curr).


scan(TokList):-
    get_char(Character),
    scan_char(Character, TokList), !.

scan_char(end_of_file, []) :- !. 
scan_char(Character, ToKlist) :-
    white(Character), !,
    get_char(C2),
    scan_char(C2, ToKlist).

scan_char(Character, [Word|TokList]):-
    category(Character, Category),
    read_word(Character, NextCharacter, '', Result,Category),
    token(Word, Result, Category),
    scan_char(NextCharacter, TokList).
    



read_word(end_of_file, end_of_file, Result, Result, _):- !.

read_word(Character, Character, Result, Result, Category) :-
    \+ category(Character, Category), !. 

read_word(FirstCharacter, NextCharacter,Temporary, Result , Category) :-
        atom_concat(Temporary, FirstCharacter, TemporaryResult),
        get_char(NewFirstCharacter),
        read_word(NewFirstCharacter, NextCharacter, TemporaryResult, Result, Category).
        



category(Character, Category) :- 
    (
        id(Character),
        Category = id
    );
    (
        key_candidate(Character),
        Category = key
    );
    (
        sep(Character),
        Category = sep
    );
    (
        int(Character),
        Category = int
    ).
    

token(Tokenized, String, id) :-
    Tokenized = id(String).
    
token(Tokenized, String, key) :-
    key(String),
    Tokenized = key(String).
    
token(Tokenized, String, sep) :-
    sep(String),
    Tokenized = sep(String).
    
token(Tokenized, String, int) :-
    int(String),
    atom_number(String, I),
    Tokenized = int(I).
    

