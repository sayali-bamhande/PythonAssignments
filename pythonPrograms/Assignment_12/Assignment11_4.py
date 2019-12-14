import logging
import os
import sys
import time
from os import path
from os.path import join
from sys import argv

from Assignment_11.CheckSumCalculator import hashfile

logFile = ""


def displayChecksum(dir):
    global logFile
    exist = os.path.isdir(dir)
    if exist:
        for folder, subFolder, files in os.walk(dir):
            logFile.write("Current directory is : %s" % dir)
            dict = {}
            for fi in files:
                file = os.path.join(folder, fi)
                file_checksum = hashfile(file)
                logFile.write("\nCheckSum of %s is " % fi)
                logFile.write(file_checksum)

                if file_checksum in dict:
                    dict[file_checksum].append(file)
                else:
                    dict[file_checksum] = [file]
            return dict
    else:
        logFile.write("Invalid path....")


def printResult(dict1):
    global logFile
    result = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(result) > 0:
        print("Found duplicate files...")
        for final in result:
            count = 0
            for node in final:
                count +=1
                if count > 1:
                    logFile.write("\n%s need to delete this file " % node)
                   # os.remove(node)
                    logFile.write("\nDeleted %s file " % node)

    else:
        logFile.write("\nThere is no duplicate file found")


def main():
    global logFile
    startTime = time.time()
    print("Developed and designed by Sayali")
    if len(argv) != 2:
        logFile.write("Wrong number of argument")
      #  exit()
    if argv[1] == "h" or argv[1] == "H":
        logFile.write("This script used to find duplicate files")
     #   exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py directory")
        print("ex: python Assignment11_4.py demo")
       # exit()
    if os.path.isdir(argv[1]):
        try:
            dir = path.realpath(argv[1])
            print(dir)
            tail, head = dir.split(argv[1])
            fpath = join(tail, "log.txt")
            logFile = open(fpath, 'w')
            fileList = displayChecksum(argv[1])
            printResult(fileList)
            endTime = time.time()
            logFile.write("\nScript took %s to execute"% (endTime-startTime))

        except Exception:
            print(Exception)
    else:
        logging.info("Invalid arguments..")


if __name__ == '__main__':
    main()
