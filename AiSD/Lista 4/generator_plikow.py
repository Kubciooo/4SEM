import string 
import random



def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generuj_plik(inserty = 100000, searche = 100000, delety = 100000):
    print(2*inserty+2*searche+2*delety)
    for i in range(inserty): 
        print("insert" + randomString(3))
    for i in range(searche):
        print("find" + randomString(3))
    for i in range(delety):
        print("delete" +randomString(3))
    for i in range(inserty): 
        print("insert" + randomString(3))
    for i in range(searche):
        print("find" + randomString(3))
    for i in range(delety):
        print("delete" +randomString(3))
        


def main():
    generuj_plik()


if __name__ == '__main__':
    main()
    