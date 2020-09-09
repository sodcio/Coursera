'''
Magic Methods
'''


import os.path
import tempfile
import random


class File:
    def __init__(self, path):
        self._path = path
        self._curr = 0
        if not os.path.exists(path):
            with open(self._path, 'w'):
                pass

            
    def __iter__(self):
        return self


    
    def __str__(self):
        return self._path



    def __add__(self, other):
        result_path = os.path.join(tempfile.gettempdir(), 'tmpfile{}.txt'.format(random.randint(0, 100)))
        result = File(result_path)
        result.write(self.read() + other.read())
        return result



    def __next__(self):
        with open(self._path, 'r', encoding='utf8') as f:
            f.seek(self._curr)
            line = f.readline()

            if line:
                self._curr = f.tell()
                return line
            else:
                self._curr = 0
                raise StopIteration
    


    def write(self, text):
        with open(self._path, 'w', encoding='utf8') as f:
            return f.write(text)
            


    def read(self):
        with open(self._path, 'r', encoding='utf8') as f:
            return f.read()

