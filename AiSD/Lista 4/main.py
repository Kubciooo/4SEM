import sys


import hmap
import rbt
import bst


def main():
    if len(sys.argv) != 3: 
        print("NIEPOPRAWNE WYWOŁANIE PROGRAMU\n")
    else: 
        if sys.argv[1] != "--type":
            print("python main.py --type rbt/hmap/bst")
        else: 
            if sys.argv[2] == "rbt":
                rbt.main()
            elif sys.argv[2] == "bst":
                bst.main()
            elif sys.argv[2] == "hmap":
                hmap.main()
            else:
                print("python main.py --type rbt/hmap/bst")


if __name__ == '__main__':
    main()
    