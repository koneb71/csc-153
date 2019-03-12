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

    def get_input(self):
        filename = raw_input("Enter File name: ")
        if filename == 'exit':
            self.running = False
        self.text = ' '.join(open(filename, 'r').readlines()).replace("\n", '')
        print(self.text)

    def check(self):
        return self.checker.is_balance(self.text)

    def tokenize(self):
        token_list = self.text.split(" ")
        cleaned_token_list = remove_emptys(token_list)
        for text in cleaned_token_list: self.stack_list.push(text)

    def print_syntax(self):
        while not self.stack_list.isempty():
            text = cleaned_text(self.stack_list.pop())
            if text in keywords:
                print('System Command: %s' % text)
            elif text in brackets:
                if self.checker.is_closing(text):
                    print('Close Bracket: %s' % text)
                elif self.checker.is_opening(text):
                    print('Open Bracket: %s' % text)
            elif self.checker.is_function_name(text):
                print('Function: %s' % text)
            elif text in symbols:
                print('Symbols: %s' % text)
            elif text in datatype:
                print('Datatype: %s' % text)
            elif text in operators:
                print('Operators: %s' % text)
            elif text in loop:
                print('Loop: %s' % text)
            elif text in returned:
                print('Return function: %s' % text)
            elif self.checker.is_number(text) or self.checker.is_float(text):
                print('Number: %s' % text)
            elif isinstance(text, str):
                print('Text: %s' % text)

    def run(self):
        while self.running:
            self.get_input()
            if self.check():
                print("Correct Syntax")
                self.tokenize()
                self.print_syntax()
            else: print("Syntax Error")

init = CCompiler()
init.run()