import json
import codecs

class Base:
    def __init__(self, data):
        for key, value in data.items():
            self.__dict__[key] = value    
    
init = json.load(codecs.open('init.json', 'r', 'utf-8-sig'))

base_master= Base(init["base_master"])

base_developer= Base(init["base_developer"])

base_dump= Base(init["base_dump"])

