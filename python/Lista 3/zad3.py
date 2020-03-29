
f = open("test.txt","r")

x = sum([int(i.split(' ')[len([i.split(' ')])-2]) for i in f.read().splitlines()])
print(x)
    