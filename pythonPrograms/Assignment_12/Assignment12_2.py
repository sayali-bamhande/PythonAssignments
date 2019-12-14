import logging
import os
import sys
from datetime import time
import psutil
from os import path
from os.path import join
from sys import argv


def isRunningProcess(processName):
    line = 40 * "-"

    fileName = "RunningLog.txt"
    obj = open(fileName, 'w')
    obj.write(line + "\n")
    obj.write("Process Logger at : %s\n" % time())
    obj.write(line + "\n")
    flag = False
    for proc in psutil.process_iter():
        if processName.lower() in proc.name().lower():
            flag = obj.write("%s is running.." % processName)
            break

    if not flag:
        obj.write("%s is not running.." % processName)

    obj.close()


def main():
    print("Developed and designed by Sayali")
    startTime = time()
    print("Developed and designed by Sayali")
    if len(argv) != 2:
        print("Wrong number of argument")
    #  exit()
    if argv[1] == "h" or argv[1] == "H":
        print("This script used to find duplicate files")
    #   exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py directory")
        print("ex: python Assignment11_4.py demo")
    isRunningProcess(argv[1])


if __name__ == '__main__':
    main()
