import filecmp
import os
import shutil
from os import path
from sys import argv


def compareFile(file1, file2):
    f1 = path.realpath(file1)
    f2 = path.realpath(file2)
    if filecmp.cmp(f1, f2):
        print("Success")
    else:
        print("Failure")


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 3:
        print("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        print("This script used to compare two files")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py file1 file2")
        print("ex: python Assignment9_1.py demo.txt test.txt")
        exit()
    if "." in argv[1] and "." in argv[2]:
        try:
            compareFile(argv[1], argv[2])
        except Exception:
            print(Exception)
    else:
        print("Invalid arguments..")


if __name__ == '__main__':
    main()
