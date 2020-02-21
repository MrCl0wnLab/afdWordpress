import collections

__slots__ = ['__atlist_attribute_color', '__atList_Http_CodeColor']


class Stylecolor:

    ''' Receita de como utilizar cores no terminal
    Ref: https://wiki.python.org.br/CoresNoTerminal
    Ref: https://www.geeksforgeeks.org/print-colors-python-terminal/
    Ref: https://en.wikipedia.org/wiki/ANSI_escape_code
    '''
    __atlist_attribute_color = {

        # TEXT COLOR
        'fg_white': '\33[37m',
        'fg_white2': '\33[97m',
        'fg_black': '\033[30m',
        'fg_red': '\033[31m',
        'fg_green': '\033[32m',
        'fg_orange': '\033[33m',
        'fg_blue': '\033[34m',
        'fg_purple': '\033[35m',
        'fg_cyan': '\033[36m',
        'fg_pink': '\033[95m',
        'fg_yellow': '\033[93m',
        'fg_light_grey': '\033[37m',
        'fg_dark_grey': '\033[90m',
        'fg_light_red': '\033[91m',
        'fg_light_green': '\033[92m',
        'fg_light_blue': '\033[94m',
        'fg_light_cyan': '\033[96m',

        # BACKGROUND COLOR
        'bg_rey': '\33[100m',
        'bg_cred': '\33[101m',
        'bg_green2': '\33[102m',
        'bg_yellow2': '\33[103m',
        'bg_blue2': '\33[104m',
        'bg_violet2': '\33[105m',
        'bg_beige2': '\33[106m',
        'bg_white2': '\33[107m',
        'bg_black': '\033[40m',
        'bg_red': '\033[41m',
        'bg_green': '\033[42m',
        'bg_orange': '\033[43m',
        'bg_blue': '\033[44m',
        'bg_purple': '\033[45m',
        'bg_cyan': '\033[46m',
        'bg_light_grey': '\033[47m',

        # PROPRIEDADES
        'end': '\033[0m',
        'bold': '\033[01m',
        'disabled': '\033[02m',
        'italic': '\33[3m',
        'underline': '\033[04m',
        'reverse': '\033[07m',
        'strike_through': '\033[09m',
        'invisible': '\033[08m',
        'blink': '\33[5m',
        'blink2': '\33[5m',
    }

    '''SET HTTP CODE COLOR
    1xx (Informational): The request was received, continuing process
    2xx (Successful): The request was successfully received, understood, and accepted
    3xx (Redirection): Further action needs to be taken in order to
    complete the request
    4xx (Client Error): The request contains bad syntax or cannot be ulfilled
     Ref: https://tools.ietf.org/html/rfc7231#section-5.5.3
    '''
    __atlist_http_CodeColor = {

        '200': __atlist_attribute_color['fg_light_green'],
        '400': __atlist_attribute_color['fg_dark_grey'],
        '401': __atlist_attribute_color['fg_dark_grey'],
        '403': __atlist_attribute_color['fg_dark_grey'],
        '404': __atlist_attribute_color['fg_red'],
        '500': __atlist_attribute_color['fg_red'],
        '501': __atlist_attribute_color['fg_dark_grey'],
        '502': __atlist_attribute_color['fg_dark_grey'],
        '503': __atlist_attribute_color['fg_dark_grey'],
        '301': __atlist_attribute_color['fg_orange'],
        '302': __atlist_attribute_color['fg_yellow'],
        '308': __atlist_attribute_color['fg_dark_grey'],
        '0': __atlist_attribute_color['fg_dark_grey'],

    }

    def __init__(self):
        ''' SET DYNAMIC ATTRIBUTE
        Ref: https://docs.python.org/3/library/stdtypes.html#object.__dict__
        Ref: https://amir.rachum.com/blog/2016/10/05/python-dynamic-attributes/
        '''
        self.__atlist_attribute_color.update(self.__atlist_http_CodeColor)
        for color_key in self.__atlist_attribute_color:
            self.__dict__[color_key] = self.__atlist_attribute_color[color_key]
