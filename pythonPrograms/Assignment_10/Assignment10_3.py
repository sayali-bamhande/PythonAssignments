import logging
import os
import shutil
from os import path
from sys import argv


def copyFiles(src_dir, dest_dir):
    logging.basicConfig(filename="logFile", level=logging.INFO, filemode='w')
    src = path.realpath(src_dir)
    os.mkdir(dest_dir)
    print("Created new directory : ", dest_dir)
    dest = path.realpath(dest_dir)
    print("path of destination directory is : ", dest)
    exist = os.path.isdir(src)
    if exist:
        for folder, subfolder, files in os.walk(src):
            for fi in files:
                print(fi)
                fname = os.path.join(src, fi)
                print(path.realpath(fname))
                shutil.copy(fname, dest)
                logging.info("Copying " + src_dir + "/" + fi + " into " + dest)


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 3:
        logging.info("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        logging.info("This script used to rename file extension")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        logging.info("Use this script like : python scriptName.py dir extension1 extension2")
        logging.info("ex: python Assignment9_1.py demo .txt .doc")
        exit()
    if os.path.isdir(argv[1]):
        try:
            copyFiles(argv[1], argv[2])
        except Exception:
            print(Exception)
    else:
        logging.info("Invalid arguments..")


if __name__ == '__main__':
    main()
