
import argparse
import csv
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('path', help='The URL to process')
    parser.add_argument('lst', help='The name of the file to store the url in')

    args = parser.parse_args()
    # print('URL:', args.url)
    # print('Destination:', args.destination)


def get_file_names(folderpath = 'tmp/', filename = 'tmp/output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file""" 
    filenames = os.listdir(folderpath)   
    with open(filename, 'w') as file:
        file.write(str(filenames))

    