
from concurrent.futures.thread import _worker
from io import UnsupportedOperation
from typing import List
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import time

class TextComparer():

    def __init__(self, url_list: List[str]):
        self.url_list = url_list
        self.filenames = [f"tmp/{url.split('/')[-1]}" for url in url_list]

    def download(self, url):         
        r = requests.get(url, stream = True)
        if (r.status_code == 202):
            print('Status code:', r.status_code)
            with open('tmp/test.txt', 'wb') as file:
                for chunk in tqdm(r.iter_content(chunk_size=1024)):
                    file.write(chunk)
        else:
            print(url)
            print('NotFoundException')

    def multi_download(self):
        workers = len(self.url_list)
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(TextComparer.download, self.url_list, self.filenames )
            print('hejsa')
        return list(res)
        
    def __iter__():
        print('iter')

    def __next__():
        print('next')

    def urlist_generator():
        with open(file) as f:
            for line in f:
                yield line.strip()
    #g = get_name_gen(file)

    def avg_vowels(text):  
        print('#Processer')
    