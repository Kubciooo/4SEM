

def transpose(m):
    return [
     ''.join([str(j+1 + int(i/2)*len(m))+"."
    +str(m[j].replace('.', ' ').split()[i])
    +(' '*min(1,len(m)-j-1))
    for j in range(len(m))])
    for i in range(1,len(m[0].replace('.', ' ').split()),2)
    ]

print(transpose( ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9", "10. 10 11.11 12.12"]))