
from concurrent.futures.thread import _worker
from io import UnsupportedOperation
from typing import List
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import time

class NotFoundException(Exception):
    pass

class TextComparer():

    def __init__(self, url_list: List[str]):
        self.url_list = url_list
        self.filenames = [] #f"tmp/{url.split('/')[-1]}" for url in url_list

    def download(self, url, filename):         
        r = requests.get(url, stream = True)
        print('Status code:', r.status_code)
        if (r.status_code != 200):
            raise NotFoundException(f" url: {url} was not found")
        else:
            with open('tmp/books/' + filename, 'wb') as file:
                for chunk in tqdm(r.iter_content(chunk_size=1024)):
                    file.write(chunk)
       
    def multi_download(self):
        workers = len(self.url_list)
        with ThreadPoolExecutor(workers) as ex:
            #ex.map(self.download, self.url_list, self.filenames )
            i = 0
            for url in self.url_list:
                filename = 'book' + str(i) + '.txt' 
                self.filenames.append(filename)
                ex.submit(self.download, url, filename)
                print(filename)
                i += 1      
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
        for url in self.url_list:
            yield url

    def avg_vowels(self, text): # Processer
        vowels = 'aeiou'
        vowel_count = 0
        word_count = 0
        with open( text, 'r') as file:
            for line in file:
                for word in line.split():
                    word_count += 1
                    for vowels in word.lower():
                        vowel_count += 1
        print('words: ', word_count)        
        print('vowels: ', vowel_count)

        number_of_vowels_per_words = (word_count / vowel_count)
        return number_of_vowels_per_words
