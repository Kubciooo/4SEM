import os
import sys
def bytes(filename):
    return os.stat(filename).st_size

def lines(filename):
     with open(filename) as file:
        x = [l.strip() for l in file]
     return len(x)

def longest_line(filename):
    longest = 0
    with open(filename) as file:
        x = [l.strip() for l in file]
    for y in x:
        longest = max(longest, len(y))
    return longest
def words(filename):
    result = 0
    with open(filename) as file:
        x = [l.strip() for l in file]
    for y in x:
        if(len(y)>0):
            z = y.split(' ')
            result = result + len(z)
    return result
        
        
f = sys.argv[1]
print("liczba bajtów: " 
    + str(bytes(f))
    + "\nliczba słów: "
    +str(words(f))+"\nliczba linii: "
    +str(lines(f))+"\nmaksymalna długość linii: "
    +str(longest_line(f))
    +"\n")