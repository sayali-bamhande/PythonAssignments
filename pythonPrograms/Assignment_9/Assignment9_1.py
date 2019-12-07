import os
from sys import argv


def searchFile(filename):
    if os.path.isfile(filename):
        print(filename, "is exist..")
    else:
        print(filename, "not exist..")


def main():
    print("Developed and designed by Sayali")
    if len(argv) < 1 or len(argv) > 2:
        print("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        print("This script used to check file exist or not")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py fileName")
        print("ex: python Assignment9_1.py demo.txt")
        exit()
    if "." in argv[1]:
        try:
            searchFile(argv[1])
        except Exception:
            print("Exception occurred...")
    else:
        print("Invalid arguments..")


if __name__ == '__main__':
    main()
