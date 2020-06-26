merge(L1, L2, Output):-
    freeze(L1, 
        freeze(L2,
            (
                L1 = [Head1|Tail1] ->
                (
                    L2 = [Head2|Tail2] ->
                    (
                        (
                            Head1 =< Head2 -> 
                            (
                                Output = [Head1|Output1],
                                merge(Tail1, L2, Output1)
                            );
                                Output = [Head2|Output1],
                                merge(L1,Tail2,Output1)
                        )
                    );
                    Output = L1
                );
                Output = L2
            )
        )
    ).