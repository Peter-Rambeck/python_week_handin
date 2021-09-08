
import argparse
import csv
import os
import sys




def get_file_names(folderpath = 'tmp/', filename = 'tmp/output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file""" 
    filenames = os.listdir(folderpath)   
    with open(filename, 'w') as file:
        file.write(str(filenames))


def get_all_file_names(folderpath = 'tmp/', filename = 'tmp/output2.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file""" 
    r = []
    for root, dirs, files in os.walk(folderpath):
        for name in files:
            r.append(os.path.join(root, name))
   
    with open(filename, 'w') as file: 
        new_r = list(reversed(r))       
        print("1" + str(r))
        print("2" + str(new_r))
        file.write(str(new_r))

    get_all_file_names(folderpath, filename)


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    n= 1
    for file in file_names:
        with open(file, 'r') as file1:
            for i in range(n):
                line_one = next(file1).strip()
                print(line_one)

                
            #for line in file1:
                #print(line.split()[0].strip())

if __name__ == '__main__':
    print_line_one(['tmp/filename.csv'])