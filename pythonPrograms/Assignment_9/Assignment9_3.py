import os
import shutil
from os import path
from sys import argv


def copyFile(filename):
    src = path.realpath(filename)
    dest = "Demo.txt"
    open(dest, "w")
    shutil.copy(src, dest)
    print("Copied to ", dest)


def main():
    print("Developed and designed by Sayali")
    if len(argv) < 2 or len(argv) > 2:
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
            copyFile(argv[1])
        except Exception:
            print("Exception occurred...")
    else:
        print("Invalid arguments..")


if __name__ == '__main__':
    main()
