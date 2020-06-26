filozofowie :-
	thread_create(filozof(0), ID1, []),
	thread_create(filozof(1), ID2, []),
	thread_create(filozof(2), ID3, []),
	thread_create(filozof(3), ID4, []),
	thread_create(filozof(4), ID5, []),
	thread_join(ID1, _),
	thread_join(ID2, _),
	thread_join(ID3, _),
	thread_join(ID4, _),
	thread_join(ID5, _).

filozof(ID) :-
	zaczyna_myslec(ID),
	Lewy is ID, %lewy widelec ma ID naszego filozofa 
	Prawy is ID + 1 mod 5, % prawy jest po prawej od filozofa 
	wypisz_akcje(ID, 'chce prawy widelec'),
	podnies_widelec(ID, Prawy, prawy),
	wypisz_akcje(ID, 'chce lewy widelec'),
	podnies_widelec(ID, Lewy, lewy),
	jedz(ID),
	odloz_widelec(ID, Prawy, prawy),
	odloz_widelec(ID, Lewy, lewy),
	filozof(ID).

wypisz_akcje(ID, Akcja):-
	mutex_lock(druk), % jak jeden filozof coś robi, to drugi czeka aż ten wypisze co ma do wypisania 
	format('[~w] ~w~n', [ID, Akcja]), %wypisujemy naszą akcję: [write(ID)] write(Akcja) endline
	mutex_unlock(druk), 
	sleep(1).

zaczyna_myslec(ID) :-
	wypisz_akcje(ID, zaczyna_mysleci).

jedz(ID):-
	wypisz_akcje(ID, 'je'). 

podnies_widelec(ID, Widelec, Strona):-
	atom_concat('w', Widelec, M), % blokujemy widelec w_Widelec - jest on zablokowany dopóki go nie odłożymy 
	mutex_lock(M),
	(
        Strona = lewy -> wypisz_akcje(ID, 'podnosi lewy widelec');	wypisz_akcje(ID, 'podnosi prawy widelec')
    ).

odloz_widelec(ID, Widelec, Strona):- 
	atom_concat('w', Widelec, M),
	(	
        Strona = lewy -> wypisz_akcje(ID, 'odklada lewy widelec');	wypisz_akcje(ID, 'odklada prawy widelec')
    ),
	mutex_unlock(M). %odkładamy nasz widelec 