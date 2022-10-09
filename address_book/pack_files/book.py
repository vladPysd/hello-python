import re

from human import Human
from logger import logging

class Address_Book:
    _dict = {}
    _index = 0
    
    def __init__(self) -> None:
        logging.debug("Creating Address Book")

    def add(self, person: Human):
        logging.debug("Adding Entry")
        self._index+=1
        dict = {self._index: person}
        self._dict.update(dict)
        
    def remove(self, index: int):
        logging.debug("Remove Entry")
        self._list.pop(index)
        
    def update(self, index: int, person: Human):
        logging.debug("Update Entry")
        if self._list.get(index) != None:
            self._list.update(index,person)
        else:
            logging.error("Entry doesn`t exists!")
            
    def __str__(self) -> str:
        lines = ""
        for i in self._dict.values():
            lines+=str(i)
        return lines