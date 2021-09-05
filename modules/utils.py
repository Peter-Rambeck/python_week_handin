
import argparse
import csv
import os
import sys

#if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
#    parser.add_argument('path', help='The path to folder')
#    parser.add_argument('filename', help='The name of the file to store the url in')

#    args = parser.parse_args()
    # print('URL:', args.url)
    # print('Destination:', args.destination)


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

if __name__ == "__main__":
    get_all_file_names(sys.argv[0], sys.argv[1])

    