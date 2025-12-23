# Date: 06/11/2025
# Program to implement a yaml file

import yaml
import os

config = {
        'photo_dir': 'photos',
        'data_dir': 'photo_info',
        'extensions': ['jpg', 'jpeg'],
    }

config_filename = 'config.yaml'
writer = open(config_filename, 'w')
yaml.dump(config, writer)
writer.close()

readback = open(config_filename).read()
print(readback)

reader = open(config_filename)
config_readback = yaml.safe_load(reader)
print(config_readback)
print()

config['data_dir']

os.makedirs(config['data_dir'], exist_ok=True)
db_file = os.path.join(config['data_dir'], 'captions')
db_file

import shelve

db = shelve.open(db_file, 'c')
db

key = 'jan-2023/photo1.jpg'
db[key] = 'Cat nose'

value =db[key]
print(value)

db[key] = 'Close up view of a cat nose'
print(db[key])

print(list(db.keys()))

key in db

for key in db:
    print(key, ':', db[key])

db.close()
print(os.listdir(config['data_dir']))
print()

def sort_word(word):
    return ''.join(sorted(word))
word = 'pots'
key = sort_word(word)
print(key)

db = shelve.open('anagram_map', 'n')
db[key] = [word]
print(db[key])

word = 'tops'
key = sort_word(word)
print(key)

anagram_list = db[key]
anagram_list.append(word)
db[key] = anagram_list
print(db[key])

path1 = 'photos/jan-2023/photo1.jpg'
data1 = open(path1, 'rb').read()
print(type(data1))

path2 = 'photos/jan-2023/photo2.jpg'
data2 = open(path2, 'rb').read()
print(data1 == data2)

def same_contents(path1, path2):
    data1 = open(path1, 'rb').read()
    data2 = open(path2, 'rb').read()
    return data1 == data2

import hashlib
md5_hash = hashlib.md5()
print(type(md5_hash))

md5_hash.update(data1)
digest = md5_hash.hexdigest()
print(digest)
print()

def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

filename2 = 'photos/feb-2023/photo2.jpg'
print(md5_digest(filename2))

# Walking Directories
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            walk(path)
walk('photos')
print()

def walk(dirname, visit_func):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            visit_func(path)
        else:
            walk(path, visit_func)
walk('photos', print)

