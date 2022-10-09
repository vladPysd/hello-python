from ctypes.wintypes import PINT


class ShortInputExcepiton(Exception):
    '''Пользоваетльский класс исключения.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Input something --> ')
    if len(text) < 3:
        raise ShortInputExcepiton(len(text), 3)
except EOFError:
    print('Why you do EOF?')
except ShortInputExcepiton as ex:
    print('ShortInputExcepiton: Length input line -- {}; \
        expect atleast -- {}'.format(ex.length, ex.atleast))