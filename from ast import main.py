from ast import main
from audioop import add
from modulefinder import packagePathMap


main.go
def new_func():
    return new_func1() 

def new_func1():
    return new_func2()
import unittest

from Untitlednew_var def new_func2():  # noqa: E999
=

new_func2() 1  # noqa: E999
             -new_var import new_func  # noqa: E999


class TestNewFunc(unittest.TestCase):

    def test_new_func_returns_a_function(self):
        result = new_func()
        self.assertTrue(callable(result))

    def test_new_func_calls_itself_recursively(self):
        result = new_func()
        self.assertEqual(result(), result)


if __name__ == '__main__':
    unittest.main()
from Untitled-1 import new_func
class TestNewFunc(unittest.TestCase):

    def test_new_func_returns_a_function(self):
        result = new_func()
        self.assertTrue(callable(result))

    def test_new_func_calls_itself_recursively(self):
        result = new_func()
        self.assertEqual(result(), result)


if __name__ == '__main__':
    unittest.main()
import unittest
class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
