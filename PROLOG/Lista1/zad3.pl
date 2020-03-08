above(b2,bicycle).
above(bicycle, pencil).
above(camera, butterfly).
left_of(pencil, hourglass).
left_of(hourglass, butterfly).
left_of(butterfly, fish).

left_off(X,Y):-left_of(X,Z),left_off(Z,Y).
left_off(X,Y):-left_of(X,Y).
abovee(X,Y):-above(X,Z),abovee(Z,Y).
abovee(X,Y):-above(X,Y).

below(X,Y):-above(Y,X).
right_of(X,Y):-left_of(Y,X).

higher(X,Y):-abovee(X,Y). /* po prostu nad w linii prostej */
higher(X,Y):-left_off(Y,Z),abovee(X,Z). /*nad w linii ale całą kolumnę bierzemy*/
higher(X,Y):-left_off(Z,Y),abovee(X,Z).
higher(X,Y):-above(X,A),above(Y,B),higher(A,B). /*X jest nad A, Y jest nad B, a A jest wyżej od B*/

