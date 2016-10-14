from unittest import TestCase
from fibonacci import *


class TestMultiples(TestCase):
    def test_fibonacci_should_return_0_when_param_is_0(self):
        assert fibonacci(0) == 0

    def test_fibonacci_should_return_89_when_param_is_11(self):
        assert fibonacci(11) == 89;

    def test_result(self):
        assert fibonacci(4000000) is not None;