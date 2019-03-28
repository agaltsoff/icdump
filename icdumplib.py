import json
import codecs

# initial settings json file name without extention

import argparse

parser = argparse.ArgumentParser(description='Выгрузка начального состояния изменений конфигурации 1С типовыми средствами')
parser.add_argument('command', metavar='COMMAND', type=str, help='Команда', choices= ['setup','commit','update','precommit','master','develop'])
parser.add_argument('--config', metavar='CONFIG', type=str, help='Файл настроек в формате json', default='.\\config.json')

args= parser.parse_args()

config_fn= args.config

class Base:
    def __init__(self, data):
        for key, value in data.items():
            self.__dict__[key] = value    
    
init = json.load(codecs.open(config_fn, 'r', 'utf-8-sig'))

base_master= Base(init["base_master"])

base_develop= Base(init["base_develop"])

base_dump= Base(init["base_dump"])

#icdump

def get_base_connect_str(params):
    return '%s /N "%s" /P "%s" /ConfigurationRepositoryF "%s" /ConfigurationRepositoryN "%s" /ConfigurationRepositoryP ""'%(params.location, params.username, params.password, params.depot_location, params.depot_username)

def get_gear(ver):
    return '"C:\\Program Files (x86)\\1cv8\\%s\\bin\\1cv8.exe" DESIGNER /DisableStartupMessages'%(ver)

GEAR= get_gear(base_dump.VER)

BASE_MASTER= get_base_connect_str(base_master)

BASE_DEVELOP= get_base_connect_str(base_develop)

# helper functions

def is_skipped(fn):
    return fn in ['Configuration.xml']

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

