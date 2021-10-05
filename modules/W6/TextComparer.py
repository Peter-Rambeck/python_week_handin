
from concurrent.futures.thread import _worker
from io import UnsupportedOperation
from typing import List
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from tqdm import tqdm
import time
import matplotlib.pyplot as plt

class NotFoundException(Exception):
    pass

class TextComparer():

    def __init__(self, url_list: List[str]):
        self.url_list = url_list
        self.filenames = []

    def download(self, url, filename):         
        r = requests.get(url, stream = True)
        print('Status code:', r.status_code)
        if (r.status_code != 200):
            raise NotFoundException(f" url: {url} was not found")
        else:
            with open(filename, 'wb') as file: # 'tmp/W6/books/' + 
                for chunk in tqdm(r.iter_content(chunk_size=1024)):
                    file.write(chunk)
       
    def multi_download(self):

        workers = len(self.url_list)
        with ThreadPoolExecutor(workers) as ex:
            i = 0
            for x in self.url_list:
                filename = 'tmp/w6/books/' + 'book' + str(i) + '.txt' 
                self.filenames.append(filename)
            #    #ex.submit(self.download, url, filename)
            #    print(filename)
                i += 1
            ex.map(self.download, self.url_list, self.filenames)      
        return self.filenames      
        
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= len(self.url_list):
            raise StopIteration
        name = self.filenames[self.counter]
        self.counter += 1
        return name

    def urlist_generator(self):
        for name in self.filenames:
            yield name

    def avg_vowels(self, text): # Processer
        vowels = 'aeiou'
        vowel_count = 0
        word_count = 0
        with open( text, 'r') as file:
            for line in file:
                #yield line
                for word in line.split():
                    word_count += 1
                    for vowels in word.lower():
                        vowel_count += 1
        print('words: ', word_count)        
        print('vowels: ', vowel_count)

        number_of_vowels_per_words = round(vowel_count/word_count, 2)
        return number_of_vowels_per_words

    def hardest_read(self):
        file_with_vowels = {}
        workers = multiprocessing.cpu_count() 
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(self.avg_vowels, self.filenames)  
            file_with_vowels.setdefault(res, self.filenames)
            print(file_with_vowels)  
        return list(res)
        
