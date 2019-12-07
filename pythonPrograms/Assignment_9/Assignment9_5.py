import filecmp
import logging
import os
import shutil
from os import path
from sys import argv


def getFrequency(file, text):
    counter = 0
    f1 = path.realpath(file)
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    with open(f1) as fobj:
        for line in fobj:
            line = line.lower()
            words = line.split(" ")
            for word in words:
                if word == text.lower():
                    counter += 1
                    print("text present")
                    logging.info("hii")
        print("Total frequency is ",counter)




def main():
    print("Developed and designed by Sayali")
    if len(argv) != 3:
        print("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        print("This script used to find frequency of String in file")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py file1 file2")
        print("ex: python Assignment9_1.py demo.txt test.txt")
        exit()
    if "." in argv[1]:
        try:
            getFrequency(argv[1], argv[2])
        except Exception:
            print(Exception)
    else:
        print("Invalid arguments..")


if __name__ == '__main__':
    main()
