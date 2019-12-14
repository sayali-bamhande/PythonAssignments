import logging
import os
import sys
from datetime import time
import psutil
from os import path
from os.path import join
from sys import argv


def displayProcessInfo():
    line = 40 * "-"

    fileName = "Log.txt"
    obj = open(fileName, 'w')
    obj.write(line + "\n")
    obj.write("Process Logger at : %s\n" %time)
    obj.write(line + "\n")

    for proc in psutil.process_iter():
        print(proc)
    obj.close()


def main():
    print("Developed and designed by Sayali")
    displayProcessInfo()


if __name__ == '__main__':
    main()
