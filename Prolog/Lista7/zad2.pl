:- consult('zad1').

split(IN, OUT1, OUT2):-
    freeze(IN,
    (
        IN = [Head|Tail] -> 
        (
            OUT1 = [Head|Tail1],
            split(Tail, OUT2, Tail1)
        );
        (
            OUT1 = [],
            OUT2 = []
        )
    )).


merge_sort(IN, OUT):-
    freeze(IN,
        (
            IN = [Head|Tail] -> 
            (
                freeze(Tail,
                (
                    Tail \= [] -> 
                    (
                        split(IN,Left,Right), % dzielimy listę na pół 
                        merge_sort(Left, Output1), % merge sort na pierwszej z nich
                        merge_sort(Right, Output2), % merge sort na drugiej 
                        merge(Output1, Output2, OUT) % posortowane listy mergujemy do OUT
                    );
                    OUT = [Head] % jeżeli mamy tylko 1 element na liscie, to go zwracamy
                ))
            );
            OUT = [] % jeżeli mamy zero elementów na lisćie, to zwracamy pustą listą 
        )
    ).