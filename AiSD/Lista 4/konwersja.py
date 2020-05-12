





def cut(message):
    key = message
    while len(key) > 0 and not key[0].isalpha():
        key = key[1:]
    while len(key) > 0 and not key[-1].isalpha():
        key = key[:-1]
    return key

with open("aspell_wordlist.txt", "r") as f: 
    content = f.read()
    print(50000)
for x in content.split()[:25000]: 
    print("insert",cut(x))
for x in content.split()[:25000]:
    print("find", cut(x))
