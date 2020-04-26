odpalenie programu jak w treści zadania. 
Do kompliacji może być potrzebna flaga -std=c++11

Przykładowe wyniki testowania - za każdym razem przeprowadzone zostało 10 000 testów: 
1) na permutacji n:
1.1)
n = 1000
i = 50
random - min: 999, max: 7344, srednia: 2355.28, odchylenie: 811.015
select - min: 4491, max: 4491, srednia: 4491, odchylenie: 0
1.2)
n = 10000
i = 100
random - min: 10118, max: 64631, srednia: 20994.5, odchylenie: 7264.17
select - min: 47446, max: 47446, srednia: 47446, odchylenie: 0

1.3)
n = 1000
i = 500
random - min: 999, max: 8065, srednia: 3328.25, odchylenie: 971.171
select - min: 4456, max: 4456, srednia: 4456, odchylenie: 0

1.4)
n = 1000
i = 1000
random - min: 999, max: 6151, srednia: 1983.46, odchylenie: 695.85
select - min: 5035, max: 5035, srednia: 5035, odchylenie: 0

1.5) 
n = 100
i = 1
random - min: 99, max: 668, srednia: 190.395, odchylenie: 68.6365
select - min: 391, max: 391, srednia: 391, odchylenie: 0

2) na losowych liczbach: 
2.1) 
n = 1000
i = 1
random - min: 999, max: 6105, srednia: 1997.19, odchylenie: 698.321
select - min: 4909, max: 4909, srednia: 4909, odchylenie: 0

2.2)
n = 1000
i = 500
random - min: 999, max: 8503, srednia: 3338.2, odchylenie: 956.718
select - min: 4463, max: 4463, srednia: 4463, odchylenie: 0
2.3)
n= 1000
i = 1000
random - min: 999, max: 6070, srednia: 1986.22, odchylenie: 699.345
select - min: 4327, max: 4327, srednia: 4327, odchylenie: 0


Wnioski: 
Nasz randomSelect średnio wykonuje mniej porównań od zwykłego selecta. Wynika to z tego, że przy dobrym doborze danych losowych może wykonać program nawet w czasie 1*n. 
Widzimy natomiast, że maksymalna liczba porównań w randomSelect jest momentami dużo większa (np. 1.3), czyli w niektórych przypadkach wykonania jest ono nawet dwukrotnie wolniejsze od zwykłego Selecta. 
Możemy zaobserwować też, że zwykły select wykonuje zawsze średnio od 4n do 5n porównań, natomiast randomSelect - od n do 8n(przy odchyleniu równym n). 