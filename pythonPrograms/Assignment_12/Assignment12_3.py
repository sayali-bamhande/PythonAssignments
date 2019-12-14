import logging
import os
import sys
from datetime import time, datetime, date
import psutil
from os import path
from os.path import join
from sys import argv


def displayProcessInfo(folder):
    line = 60 * "-"
    if not os.path.isdir(folder):
        os.mkdir(folder)

    dirPath = path.realpath(folder)
    #now = datetime.now()
    current_time = str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    fileName = join(dirPath, "processLog.log_" + current_time)
    obj = open(fileName, 'w')
    obj.write(line + "\n")
    obj.write("Process Logger at : %s\n" % str(datetime.now().strftime("%Y / %m / %d %H:%M:%S")))
    obj.write(line + "\n")

    for proc in psutil.process_iter():
        obj.write(str(proc))
        obj.write("\n")
    obj.close()


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 2:
        print("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        print("This script used to get process details and send it to email id")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py directory emailID")
        print("ex: python Assignment10_1.py demo")
        exit()
    if not os.path.isdir(argv[1]):
        try:

            dir = path.realpath(argv[1])
            print(dir)
            displayProcessInfo(dir)
        # logFile.write("\nScript took %s to execute" % (endTime - startTime))

        except Exception:
            print(Exception)
    displayProcessInfo(argv[1])


if __name__ == '__main__':
    main()
