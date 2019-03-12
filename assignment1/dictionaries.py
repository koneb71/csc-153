import re

keywords = ['print', 'scanf', '#include', "stdio.h", 'main', 'do', 'return', 'while', 'for']
loop = ['do', 'while', 'for']
returned = ['return']
datatype = ['int', 'float', 'char', 'double', 'string']
brackets = ['(', ')', '{', '}']
symbols = ['#', '%', '?',  ';', '.', '_', '"', "'"]
operators = ['+', '/', '*', '-', '>', '<', '=', '!']


class SyntaxChecker(object):
    def __init__(self):
        self.keywords = keywords
        self.symbols = symbols
        self.operators = operators

    def is_balance(self, string):
        symbols_list = ['(', ')', '{', '}', '[', ']', '"', "'"]
        for br in symbols_list:
            string = string.replace(br, '')
        for x in symbols_list:
            if x in string:
                return False
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
