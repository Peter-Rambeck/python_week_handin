import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('path', help='The folder-path and filename')
    parser.add_argument('lst', help='a list of elements') # nargs='+', default=[1, 2, 3]

    args = parser.parse_args()
    # print('URL:', args.url)
    # print('Destination:', args.destination)

def write_list_to_file3(args):
    print(args.path)
    print(args.lst)

    with open(args.path, 'w') as file3:
        file_write = csv.writer(file3 ) #delimiter = '\n'
        file_write.writerow(args.lst)

write_list_to_file3(args)



