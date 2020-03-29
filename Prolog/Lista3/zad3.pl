even_permutation( [], [] ).     %[] => [] ma 0 cykli, czyli jest parzystą permutacją 
even_permutation( [X|T], Perm ) :-  %parzysta permutacja N+1 elementów jest wtedy, kiedy: 
    even_permutation( T, Perm1 ),   %1. Mamy parzystą permutację dla N elementów 
    insert_odd( X, Perm1, Perm ).   % i dodamy do niej n+1 element w nieparzystym miejscu
even_permutation( [X|T], Perm ) :-  
    odd_permutation( T, Perm1 ),    %2. mamy nieparzystą permutację N elementową
    insert_even( X, Perm1, Perm ).  % i dodamy do niej parzysty element 

odd_permutation( [X|T], Perm ) :-    %nieparzysta permutacja n+1 elementów jest wtedy, kiedy:
    odd_permutation( T, Perm1 ),    % 1. N-elementowa permutacja jest nieparzysta
    insert_odd( X, Perm1, Perm ).   % i dodamy do niej element na nieparzystym miejscu
odd_permutation( [X|T], Perm ) :-   
    even_permutation( T, Perm1 ),   %2. mamy parzystą N-elementową permutację
    insert_even( X, Perm1, Perm ).  % i dodamy do niej parzysty element 

insert_odd( X, InList, [X|InList] ).        % X dajemy w nieparzystych miejscach listy(numerujemy od 1)
insert_odd( X, [Y,Z|InList], [Y,Z|OutList] ) :-
    insert_odd( X, InList, OutList ).

insert_even( X, [Y|InList], [Y,X|InList] ). % X dajemy w parzystych miejscach listy, takie wstawienie zmieni nam parzystość
insert_even( X, [Y,Z|InList], [Y,Z|OutList] ) :-
    insert_even( X, InList, OutList ).