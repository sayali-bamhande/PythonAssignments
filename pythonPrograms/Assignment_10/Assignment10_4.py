import logging
import os
import shutil
from os import path
from sys import argv


def copyFiles(src_dir, dest_dir, extension):
    logging.basicConfig(filename="logFile", level=logging.INFO, filemode='w')
    src = path.realpath(src_dir)
    os.mkdir(dest_dir)
    print("Created new directory : ", dest_dir)
    dest = path.realpath(dest_dir)
    print("path of destination directory is : ", dest)
    exist = os.path.isdir(src)
    if exist:
        fileCount = 0
        for folder, subfolder, files in os.walk(src):

            for fi in files:
                if extension in fi:
                    fileCount +=1
                    fname = os.path.join(src, fi)
                    print(path.realpath(fname))
                    shutil.copy(fname, dest)
                    logging.info("Copying " + src_dir + "/" + fi + " into " + dest)
        if fileCount == 0:
            logging.info("File not found with " + extension)


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 4:
        logging.info("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        logging.info("This script used to copy .extension files from src to destination")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        logging.info("Use this script like : python scriptName.py dir1 dir2 extension")
        logging.info("ex: python Assignment9_1.py demo demo1 .txt")
        exit()
    if os.path.isdir(argv[1]) and "." in argv[3]:
        try:
            copyFiles(argv[1], argv[2], argv[3])
        except Exception:
            print(Exception)
    else:
        logging.info("Invalid arguments..")


if __name__ == '__main__':
    main()
