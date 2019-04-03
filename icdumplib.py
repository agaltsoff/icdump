import os
import json
import codecs
import shutil
import os
import subprocess
import argparse

class Base:
    def __init__(self, data):
        for key, value in data.items():
            self.__dict__[key] = value    
    
def get_base_connect_str(params):
    return '%s /N "%s" /P "%s" /ConfigurationRepositoryF "%s" /ConfigurationRepositoryN "%s" /ConfigurationRepositoryP ""'%(params.location, params.username, params.password, params.depot_location, params.depot_username)

def get_gear(ver):
    return '"C:\\Program Files (x86)\\1cv8\\%s\\bin\\1cv8.exe" DESIGNER /DisableStartupMessages'%(ver)

def is_skipped(fn):
    return fn in ['Configuration.xml']

def debug_remove(fn):
    print('<-', fn)

def debug_makedirs(fn):
    print('++', fn)

def debug_copy(src, dst):
    print(src, '->', dst)

commands= {
    'setup'     : 'Начальная выгрузка эталона',
    'update'    : 'Выгрузка изменений эталона',
    'precommit' : 'Выгрузка отличий разработки от эталона',
    'master'    : 'Перенос отличий из эталона в репозиторий',
    'develop'   : 'Перенос отличий из разработки в репозиторий',
    'checkout'  : 'Загрузка файлов репозитория в конфигурацию разработки',
    'rollback'  : 'Отмена изменений конфигурации разработки',
    'commit'    : 'git commit (не реализовано)',
}

parser = argparse.ArgumentParser(description='Выгрузка начального состояния изменений конфигурации 1С типовыми средствами', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('command', metavar='COMMAND', type=str, nargs= '+', choices= commands.keys(), help='\n'.join("%s\t%s" % (name, descr) for (name, descr) in commands.items()))
parser.add_argument('--config', metavar='CONFIG', type=str, help='Файл настроек в формате json', default='.\\config.json')
parser.add_argument('--path', metavar='PATH', type=str, help='Рабочий каталог', default='.\\')
parser.add_argument('--debug', help='Режим отладки', action="store_true")

args= parser.parse_args()

config_fn= args.config

init = json.load(codecs.open(os.path.join(args.path, config_fn), 'r', 'utf-8-sig'))

base_master= Base(init["base_master"])

base_develop= Base(init["base_develop"])

base_dump= Base(init["base_dump"])

GEAR= get_gear(base_dump.VER)

BASE_MASTER= get_base_connect_str(base_master)

BASE_DEVELOP= get_base_connect_str(base_develop)

if args.debug:
    shutil.copy= debug_copy
    os.remove= debug_remove
    os.makedirs= debug_makedirs
    subprocess.call= print


