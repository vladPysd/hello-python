import re

from exception import ValidateException


class Human:
    def __init__(self, name, address, phone) -> None:
        Human.validate_name(name)
        Human.validate_phone(phone)
        self.name = name
        self.address = address
        self.phone = phone
        
    @staticmethod
    def validate_name(name):
       whitespacesList = re.findall(r"\b\s\b", name) 
       if len(whitespacesList)>0:
           raise ValidateException("Invalid input name")
       
    @staticmethod
    def validate_phone(phone):
        symbolList = re.findall(r"([a-zA-Z\-\+\_\%\$\#\s])+", phone)
        if len(symbolList) > 0:
            raise ValidateException("Invalid phone number. Contains non digit symbols")
    def __str__(self) -> str:
        return 'name: {} address: {} phone: {}\n'.format(self.name, self.address, self.phone)