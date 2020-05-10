import time
import math
def calculate_time(func):
    print("dodano")
    def inner(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        time_taken = time.time() - start
        print("Czas wykonania: ",time_taken,"s")
    return inner 

@calculate_time
def czekaj_n_sekund(n):
    time.sleep(n)
    print("poczekałem!")


x = int(input())
czekaj_n_sekund(x)

