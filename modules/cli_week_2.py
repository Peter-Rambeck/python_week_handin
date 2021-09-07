import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that a file path and name, and a list of elements to store locally in the the given file')
    parser.add_argument('path', help='The folder-path and filename')
    parser.add_argument('lst', help='a list of elements') # nargs='+', default=[1, 2, 3]

    args = parser.parse_args()
    # print('URL:', args.url)
    # print('Destination:', args.destination)

def write_list_to_file3(path, *lst: list):
    print(path)
    print(lst)

    with open(path, 'w') as file3:
        file_write = csv.writer(file3) #delimiter = '\n'
        file_write.writerow(lst)

write_list_to_file3(args.path, args.lst)



