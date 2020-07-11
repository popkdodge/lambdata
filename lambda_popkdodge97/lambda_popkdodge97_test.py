#!/usr/bin/env python
"""Tests for lambdata modules."""
import unittest
# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)
# Other types of tests (you won't write now, just to be aware):
# - Integration: testing multiple pieces working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code tests that are common
# - User acceptance testing: show it to a user, get feedback
# - Manual running and checking
from example_module import increment
class ExampleModuleTests(unittest.TestCase):
    """Making sure our example module works as expected."""
    def test_increment(self):
        """Testing that the increment function adds one to a number."""
        # Unit tests work by having some logic/values
        # that use the code being tested
        x1 = 7
        y1 = increment(x1)
        x2 = -10
        y2 = increment(x2)
        # And then making sure the output is as expected with assertions
        self.assertEqual(y1, 8)
        self.assertEqual(y2, -9)
if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()