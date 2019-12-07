import logging
import os
from os import path
from os.path import realpath, join
from sys import argv


def renameExtension(dirname, extension1, extension2):
    f1 = path.realpath(dirname)
    exist = os.path.isdir(f1)
    logging.basicConfig(filename="logFile", level=logging.INFO, filemode='w')
    if exist:
        for folder, subFolder, files in os.walk(f1):
            for f in subFolder:
                print("sub folder : ", f)
            for fi in files:
                if extension1 in fi:
                    logging.info("Found file with " + extension1 + "->" + fi)
                    newfile = fi.replace(extension1, extension2)
                    path1 = realpath(folder)
                    os.rename(join(path1, fi), join(path1, newfile))
                    logging.info("Found file with " + extension1 + "->" + fi)
                    logging.info("Renaming into " + extension2 + "->" + fi)


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 4:
        logging.info("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        logging.info("This script used to rename file extension")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        logging.info("Use this script like : python scriptName.py dir extension1 extension2")
        logging.info("ex: python Assignment9_1.py demo .txt .doc")
        exit()
    if "." in argv[2] and "." in argv[3] and os.path.isdir(argv[1]):
        try:
            renameExtension(argv[1], argv[2], argv[3])
        except Exception:
            print(Exception)
    else:
        logging.info("Invalid arguments..")


if __name__ == '__main__':
    main()
