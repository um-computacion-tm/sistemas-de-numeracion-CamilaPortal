import unittest
from sistNume import decimal2binario
from sistNume import binario2decimal

class TestDecimalBinario(unittest.TestCase):
    def test_1(self):
        result = decimal2binario(36)
        self.assertEqual(result, "100100")

    def test_2(self):
        result = decimal2binario(97)
        self.assertEqual(result, "1100001")
    
    def test_3(self):
        result = decimal2binario(100)
        self.assertEqual(result, "1100100")

    def test_4(self):
        result = decimal2binario(168)
        self.assertEqual(result, "10101000")

class TestBinarioDecimal(unittest.TestCase):
    def test1(self):
        result = binario2decimal(100100)
        self.assertEqual(result, 36)

    def test2(self):
        result = binario2decimal(1100001)
        self.assertEqual(result, 97)
    
    def test3(self):
        result = binario2decimal(1100100)
        self.assertEqual(result, 100)

    def test4(self):
        result = binario2decimal(10101000)
        self.assertEqual(result, 168)

if __name__ == '__main__':
    unittest.main()