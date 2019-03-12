# C compiler
import sys

from stack import ListStack as Stack
from dictionaries import *
from utils import *

class CCompiler(object):
    def __init__(self):
        self.stack_list = Stack()
        self.text = ''
        self.checker = SyntaxChecker()
        self.running = True
        self.tokenize_list = []

    def get_filename(self):
        filename = raw_input("Enter File name (E.g. 'code.txt'): ")
        if filename == 'exit':
            self.running = False
        self.text = '\n'.join(open(filename, 'r').readlines())
        print(self.text)

    def select_index(self):
        select = raw_input("Select Index: ")
        if select == 'exit' or select.isalpha():
            self.running = False
        else:
            selected = self.tokenize_list[int(select)]
            print(list_of_keywords[selected[0]][selected[1]])

    def pop_cleaned_text(self):
        text = self.stack_list.pop()
        if ';' in text:
            self.tokenize_list.append(('symbol', global_symbols.index(';')))
        return text.replace("  ", '').replace(';', '').replace('"', '').replace("'", '')

    def check(self):
        return self.checker.is_balance(self.text)

    def tokenize(self):
        token_list = self.text.split("\n")
        cleaned_token_list = remove_emptys(token_list)

        for text in cleaned_token_list:
            if '"' in text or "'" in text:
                if '"' in text:
                    cleaned_string = text.split('"')[1]
                    self.stack_list.push(cleaned_string)
                if "'" in text:
                    cleaned_string = text.split("'")[1]
                    self.stack_list.push(cleaned_string)
            else:
                for string in text.split(' '):
                    self.stack_list.push(string)
        self.stack_list.remove_empties()

    def tokenize_syntax(self):
        while not self.stack_list.isempty():
            text = self.pop_cleaned_text()
            if text in keywords:
                self.tokenize_list.append(('reservedKeyword', global_keywords.index(text)))
            elif text in brackets:
                if self.checker.is_closing(text):
                    self.tokenize_list.append(('symbol', global_symbols.index(text)))
                elif self.checker.is_opening(text):
                    self.tokenize_list.append(('symbol', global_symbols.index(text)))
            elif self.checker.is_function_name(text):
                if not text in functions:
                    functions.append(text)
                self.tokenize_list.append(('function', functions.index(text)))
            elif text in symbols:
                self.tokenize_list.append(('symbol', global_symbols.index(text)))
            elif text in datatype:
                self.tokenize_list.append(('datatype', datatype.index(text)))
            elif text in operators:
                self.tokenize_list.append(('operator', operators.index(text)))
            elif text in loop:
                self.tokenize_list.append(('reservedKeyword', global_keywords.index(text)))
            elif text in returned:
                self.tokenize_list.append(('reservedKeyword', global_keywords.index(text)))
            elif self.checker.is_number(text) or self.checker.is_float(text):
                if not text in numbers:
                    numbers.append(text)
                self.tokenize_list.append(('number', numbers.index(text)))
            elif isinstance(text, str):
                if not text in strings:
                    strings.append(text)
                self.tokenize_list.append(('string', strings.index(text)))

    def run(self):
        self.get_filename()
        if self.check():
            print("Correct Syntax")
            self.tokenize()
            self.tokenize_syntax()
        else:
            print("Syntax Error")
        print(self.tokenize_list)
        while self.running:
            try:
                self.select_index()
            except:
                print("Wrong Input!")