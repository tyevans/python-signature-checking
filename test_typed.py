#!/usr/bin/python
from unittest import TestCase
from sigcheck import typed

@typed
def test_func(a: int, b: float, *args: int, **kwargs: str):
    if a > 5:
        return "string"
    return a

class TestTyped(TestCase):
    def test_typed(self):
        self.assertEqual( test_func(3, 5.0), 3)
        self.assertEqual( test_func(3, 5.0, 5), 3)
        self.assertRaises(TypeError, test_func, "hello", 5.0)
        self.assertEqual( test_func(3, 5.0, 5), 3)
        self.assertRaises(TypeError, test_func, 3, 5.0, "meh")
        self.assertRaises(TypeError, test_func, 3, 5.0, 3, foo=4)
        self.assertEqual(test_func(3, 5.0, 3, foo="yay!"), 3)
