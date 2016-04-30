from unittest import TestCase
from fibonacci_strings import FibonacciStrings


class TestFibonacciStrings(TestCase):
    def test_generate(self):
        fbs = FibonacciStrings()
        self.assertEqual( fbs.generate(), 'b')
        self.assertEqual( fbs.generate(1), 'a')
        self.assertEqual( fbs.generate(2), 'ab')
        self.assertEqual( fbs.generate(2), 'ab')
        self.assertEqual( fbs.generate(3), 'aba')
        self.assertEqual( fbs.generate(5) , 'abaababa')
        self.assertEqual( fbs.generate(1, second='c'), 'c')
        self.assertNotEqual(fbs.generate(1, first='c'), 'c')
        self.assertEqual(fbs.generate(5, first='a', second='b'), 'babbabab')
        self.assertEqual(len(fbs.generate_length(500)), 500)

        #self.fail()
