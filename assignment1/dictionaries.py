import re

keywords = ['print', 'scanf', '#include', "stdio.h", 'main']
loop = ['do', 'while', 'for']
returned = ['return']
datatype = ['int', 'float', 'char', 'double', 'string']
brackets = ['(', ')', '{', '}']
symbols = ['#', '%', '?',  ';', '.', '_', '"', "'"]
operators = ['+', '/', '*', '-', '>', '<', '=', '!']

global_symbols = ['#', '%', '?',  ';', '.', '_', '"', "'", '(', ')', '{', '}']
global_keywords = ['print', 'scanf', '#include', "stdio.h", 'main', 'do', 'return', 'while', 'for']
functions = []
strings = []
numbers = []

list_of_keywords = {
    'reservedKeyword': global_keywords,
    'symbol': global_symbols,
    'datatype': datatype,
    'operator': operators,
    'string': strings,
    'function': functions,
    'number': numbers,
}

class SyntaxChecker(object):
    def __init__(self):
        self.keywords = keywords
        self.symbols = symbols
        self.operators = operators

    def is_balance(self, string):
        symbols_list = ['()', '{}', '[]']
        for br in symbols_list:
            counter = [0, 0]
            for k, v in enumerate(br):
                if v in string:
                    counter[k] += 1
            if counter[0] != counter[1]: return False

        quotes_list = ['"', "'"]
        for v in quotes_list:
            if v in string and string.count(v) % 2 != 0: return False
        return True

    def is_closing(self, string):
        return True if string in ['}', ')', ']'] else False

    def is_opening(self, string):
        return True if string in ['{', '(', '['] else False

    def is_function_name(self, string):
        return re.match(r"[a-zA-z]+\(.*\)", string)

    def is_number(self, string):
        return string.isdigit()

    def is_float(self, string):
        try:
            num = float(string)
            if num: return True
        except:
            return False
