import json
import codecs

# initial settings json file name without extention
profile= 'init' 

class Base:
    def __init__(self, data):
        for key, value in data.items():
            self.__dict__[key] = value    
    
init = json.load(codecs.open(profile + '.json', 'r', 'utf-8-sig'))

base_master= Base(init["base_master"])

base_develop= Base(init["base_develop"])

base_dump= Base(init["base_dump"])

# debug

import shutil
import os

if "debug" in init:
    debug= init["debug"]
else:
    debug= False

def debug_remove(fn):
    print('<-', fn)

def debug_makedirs(fn):
    print('++', fn)

def debug_copy(scr, dst):
    print(src, '->', dst)

if debug:
    shutil.copy= debug_copy
    os.remove= debug_remove
    os.makedirs= debug_makedirs
