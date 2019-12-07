import logging
import os
from os import path
from sys import argv


def displayFileName(dirname, extension):
    f1 = path.realpath(dirname)
    exist = os.path.isdir(f1)
    print(f1)
    logging.basicConfig(filename="logFile", level=logging.INFO, filemode='w')
    if exist:
        for folder, subFolder, files in os.walk(f1):
            for f in subFolder:
                print("sub folder : ", f)
            for fi in files:
                if extension in fi:
                    logging.info("Found file with " + extension + "->" + fi)


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 3:
        logging.info("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        logging.info("This script used to display files which has extension passed by user")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        logging.info("Use this script like : python scriptName.py dir extension")
        logging.info("ex: python Assignment9_1.py demo .txt")
        exit()
    if "." in argv[2] and os.path.isdir(argv[1]):
        try:
            displayFileName(argv[1], argv[2])
        except Exception:
            print(Exception)
    else:
        logging.info("Invalid arguments..")


if __name__ == '__main__':
    main()
