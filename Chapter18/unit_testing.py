# Date: 06/12/2025
# Program to implement unit testing

def add(a, b):
    '''Add two numbers.

    >>> add(2, 2)
    4
    '''
    return a + b

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)
run_doctests(add)

from unittest import TestCase

class TestExample(TestCase):

    def test_add(self):
        result = add(2, 2)
        self.assertEqual(result, 4)
    def test_add_broken(self):
        result = add(2, 2)
        self.assertEqual(result, 100)

import unittest

def run_unittest():
    unittest.main(argv=[''], verbosity=0, exit=False)

run_unittest()
