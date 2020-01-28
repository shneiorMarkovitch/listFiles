from os import listdir
from os.path import isfile, join, isdir
import os
import csv
import time

starting_path = 'C:\Program Files\AVAST Software\Avast'
expr_list = ['XT.ec', 'AcGenral', 'ERRORREP', 'CSC', 'dll', 'pak']

with open('fileList.csv', 'w', newline=''):
    pass

def get_file_list(path):
    files_list = [f for f in listdir(path) if isfile(join(path, f))]
    folder_list = [f for f in listdir(path) if isdir(join(path, f))]
    for file in files_list:
        for expr in expr_list:
            if expr in file:
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path + '\\' + file)
                stats = [path, file, time.ctime(ctime), time.ctime(mtime), time.ctime(atime)]
                writeOnCsv(stats)
                break
    for folder in folder_list:
        get_file_list(path + '\\' + folder)

def writeOnCsv(row):
    with open('fileList.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

get_file_list(starting_path)
