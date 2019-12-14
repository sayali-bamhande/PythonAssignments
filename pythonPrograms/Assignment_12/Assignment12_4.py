import logging
import os
import sys
from datetime import time, datetime, date
import psutil
from os import path
from os.path import join
from sys import argv

from Assignment_12.emailWithAttachment import isConnected, mailSender


def displayProcessInfo(folder):
    line = 60 * "-"
    if not os.path.isdir(folder):
        os.mkdir(folder)

    dirPath = path.realpath(folder)
    current_time = str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    file = "processLog_" + current_time+".log"
    fileName = join(dirPath, file)
    obj = open(fileName, 'w')
    obj.write(line + "\n")
    obj.write("Process Logger at : %s\n" % str(datetime.now().strftime("%Y / %m / %d %H:%M:%S")))
    obj.write(line + "\n")

    for proc in psutil.process_iter():
        obj.write(str(proc))
        obj.write("\n")
    obj.close()
    tail,head = fileName.split(dirPath)
    return join(folder, file)


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
    if os.path.isdir(argv[1]):
        try:

            dir = path.realpath(argv[1])
            print(dir)
            file = displayProcessInfo(dir)
            print("Get filename : ",file)
        # logFile.write("\nScript took %s to execute" % (endTime - startTime))
            emailId = "sayali.bamhande@gmail.com"
            pwd = "******"
            connected = isConnected()
            t = "hello"
            if connected:

                to = "sayali.bamhande@gmail.com"
                mailSender(emailId, pwd, to, file)
            else:
                print("No internet....")

        except Exception:
            print(Exception)
    else:
        print("%s already exist"%argv[1])


if __name__ == "__main__":
    main()
