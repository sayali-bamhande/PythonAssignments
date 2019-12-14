import logging
import os
import sys
from datetime import time, datetime, date
import psutil
from os import path
from os.path import join
from sys import argv
import time

import schedule as schedule

from Assignment_11.CheckSumCalculator import hashfile


from Assignment_13.emailWithAttachment import isConnected, mailSender


def displayChecksum(dir):
    exist = os.path.isdir(dir)

    if exist:
        for folder, subFolder, files in os.walk(dir):
            print("Current directory is : %s" % dir)
            dict = {}
            for fi in files:
                file = os.path.join(folder, fi)
                file_checksum = hashfile(file)
                # logFile.write("\nCheckSum of %s is " % fi)
                print("\nCheckSum of %s is " % fi)
                print(file_checksum)

                if file_checksum in dict:
                    dict[file_checksum].append(file)
                else:
                    dict[file_checksum] = [file]
            return dict
    else:
        print("Invalid path....")


def deleteDuplicateFiles(dict,fileLocation):
    line = 60 * "-"
    current_time = str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    file = "processLog_" + current_time + ".txt"
    fileName = join(fileLocation, file)
    obj = open(fileName, 'w')
    obj.write(line + "\n")
    obj.write("Process Logger at : %s\n" % str(datetime.now().strftime("%Y / %m / %d %H:%M:%S")))

    dict1 = displayChecksum(dict)
    result = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(result) > 0:
        print("Found duplicate files are as below...")
        for final in result:
            count = 0
            for node in final:
                count +=1
                if count > 1:
                    #obj.write("\n%s need to delete this file " % node)
                    print("\n%s need to delete this file " % os.path.basename(node))
                    os.remove(node)
                    obj.write("\n%s" % os.path.basename(node))
                    print("\nDeleted %s file " % node)

    else:
        obj.write("\nThere is no duplicate file found")

    obj.close()
    return [obj,fileName]


def main():
    print("Developed and designed by Sayali")
    if len(argv) != 4:
        print("Wrong number of argument")
        exit()
    if argv[1] == "h" or argv[1] == "H":
        print("This script used to get process details and send it to email id")
        exit()
    if argv[1] == "u" or argv[1] == "U":
        print("Use this script like : python scriptName.py directory time emailID")
        print("ex: python Assignment10_1.py demo 10 abc@xyz.com")
        exit()
    if os.path.isdir(argv[1]):
        try:
            name = "Marvellous"
            if not os.path.isdir(name):
                os.mkdir(name)

            print("Created new directory with name %s"% name)
            filepath = path.realpath(name)
            print("path of destination directory is : ", filepath)
            obj = deleteDuplicateFiles(argv[1],filepath)
            recepientName,tail = argv[3].split('@')
            emailSubject = "Assignment13_1 : Duplicate files name"
            body = """Hello %s
                   Please find the attachment which contains name of 
                   duplicate files.
                   We have deleted these duplicate files from %s directory
                   
                   Thanks""" % (recepientName, argv[1])
            mailSender(argv[3],obj[1],emailSubject,body)
        #     else:
        #         print("No internet....")

        except Exception:
            print(Exception)
    else:
        print("%s already exist"%argv[1])


if __name__ == "__main__":
    schedule.every(int(argv[2])).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)

