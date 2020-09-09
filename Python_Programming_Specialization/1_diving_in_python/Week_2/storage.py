import argparse
import json
import os
import sys
import tempfile 

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

class Storage_class:
    def __init__(self):
        if not os.path.isfile(storage_path): 
            self.storage = dict()
        else:
            with open(storage_path) as f:
                self.storage = json.load(f)

    def save(self):
        with open(storage_path, 'w') as f:
            json.dump(self.storage, f)

    def add(self, key, value):
        if key not in self.storage:
            self.storage[key] = list()
        self.storage[key].append(value)

    def get(self, key):
        if key in self.storage:
            return ', '.join(self.storage[key])
        
        else:
            return None

argparser = argparse.ArgumentParser(description='')
argparser.add_argument('-k', '--key', help='key', action='store', dest='key', required=True)
argparser.add_argument('-v', '--value', help='value', action='store', dest='value')
args = argparser.parse_args()

Storage = Storage_class()

if args.value is None:
    print(Storage.get(args.key))
else:
    Storage.add(args.key, args.value)
    Storage.save()
