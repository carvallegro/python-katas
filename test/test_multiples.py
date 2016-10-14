from unittest import TestCase
from numbers import *

class TestMultiples(TestCase):
    def test_multiples_should_return_0_when_None_parameter(self):
        assert multiples(None) == 0

    def test_multiples_should_return_0_when_0_parameter(self):
        assert multiples(0) == 0

    def test_multiples_should_return_3_when_3_parameter(self):
        assert multiples(4) == 3;

    def test_multiples_should_return_8_when_5_parameter(self):
        assert multiples(6) == 8;

    def test_multiples_should_return_23_when_10_parameter(self):
        assert multiples(10) == 23;