#in the module file write a function with a generator, that can serve one name at a time (like you created in the last lesson)
import pandas as pd
from pandas.io import excel

file = pd.read_excel('/home/tha/ghub/4sem/python/2020s/unisex_navne.xls', header=None, names=['navne'])['navne']

def read_file(file):
    names = []
    with open(file, 'r') as file:
        reader = excel.reader(file) #delimiter = '\t'
        for row in reader:
            yield row
            print(str(row))
read_file(file)


def read_linewise(path):
    with open(path) as fp:
        for line in fp:
            yield line


#    for n len(file):
#        yield names
#        num += 1

#[x for x in firstn(10)]
#fn = firstn(10)
#print(next(fn))
#print(next(fn))