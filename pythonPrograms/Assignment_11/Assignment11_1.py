import logging
import os
import sys
from os import path
from os.path import join
from sys import argv

from Assignment_11.CheckSumCalculator import hashfile


def displayChecksum(dirname):
    dir = path.realpath(dirname)
    print(dir)
    tail,head = dir.split(dirname)
    fpath = join(tail, "logfile.log")
    logFile = open(fpath, 'w')
    exist = os.path.isdir(dir)
    if exist:
        for folder, subFolder, files in os.walk(dir):
            print("Current directory is :", dir)
            for fi in files:
                file = os.path.join(folder, fi)
                #  add(2,3)
                file_checksum = hashfile(file)
                print("CheckSum of ", fi, "=", file_checksum)
                logFile.write("\nCheckSum of %s is " % fi)
                logFile.write(file_checksum)


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 2:
        logging.info("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        logging.info("This script used to display checksum of all files")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        logging.info("Use this script like : python scriptName.py directory")
        logging.info("ex: python Assignment10_1.py demo")
        exit()
    if os.path.isdir(argv[1]):
       # try:
            displayChecksum(argv[1])
        # except Exception:
        #     print(Exception)
    else:
        logging.info("Invalid arguments..")


if __name__ == '__main__':
    main()
