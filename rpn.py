#!/usr/bin/env python3

import operator
import logging
import sys
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '!': math.factorial,
    '++': math.fsum,
}

def calculate(arg):
    stack = list()

    for token in arg.split():
        try:
            value = float(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            #this if will grow to include other
            #single-arg operators
            try:
                if function == math.factorial:
                    arg = stack.pop()
                    result = function(arg)
                elif function == math.fsum:
                    result = function(stack)
                    stack = list()
                else:
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result = function(arg1, arg2)
                stack.append(result)
            except ZeroDivisionError:
                print('Error: divide by zero')
        logger.debug(stack)
  
    if len(stack) != 1:
        raise TypeError

    return stack.pop()

def main():
    while True:
        print(calculate(input('rpn calc> ')))
           

if __name__ == '__main__':
    main()
