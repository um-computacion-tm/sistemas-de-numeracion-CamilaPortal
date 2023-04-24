import unittest

from sistNume import decimal2binario
from sistNume import decimal2hexadecimal
from sistNume import decimal2octal

from sistNume import binario2decimal
from sistNume import binario2hexadecimal
from sistNume import binario2octal

from sistNume import hexadecimal2decimal
from sistNume import hexadecimal2binario
from sistNume import hexadecimal2octal

from sistNume import octal2decimal
from sistNume import octal2binario
from sistNume import octal2hexadecimal

class TestDecimalBinario(unittest.TestCase):
    def test1(self):
        result = decimal2binario(36)
        self.assertEqual(result, "100100")

    def test2(self):
        result = decimal2binario(97)
        self.assertEqual(result, "1100001")
    
    def test3(self):
        result = decimal2binario(100)
        self.assertEqual(result, "1100100")

    def test4(self):
        result = decimal2binario(168)
        self.assertEqual(result, "10101000")


class TestDecimalHexadecimal(unittest.TestCase):
    def test5(self):
        result = decimal2hexadecimal(500)
        self.assertEqual(result, "1F4")

    def test6(self):
        result = decimal2hexadecimal(97)
        self.assertEqual(result, "61")
    
    def test7(self):
        result = decimal2hexadecimal(100)
        self.assertEqual(result, "64")

    def test8(self):
        result = decimal2hexadecimal(168)
        self.assertEqual(result, "A8")

class TestDecimalOctal(unittest.TestCase):
    def test9(self):
        result = decimal2octal(500)
        self.assertEqual(result, "764")

    def test10(self):
        result = decimal2octal(97)
        self.assertEqual(result, "141")
    
    def test11(self):
        result = decimal2octal(100)
        self.assertEqual(result, "144")

    def test12(self):
        result = decimal2octal(168)
        self.assertEqual(result, "250")

class TestBinarioDecimal(unittest.TestCase):
    def test13(self):
        result = binario2decimal(100100)
        self.assertEqual(result, 36)

    def test14(self):
        result = binario2decimal(1100001)
        self.assertEqual(result, 97)
    
    def test15(self):
        result = binario2decimal(1100100)
        self.assertEqual(result, 100)

    def test16(self):
        result = binario2decimal(10101000)
        self.assertEqual(result, 168)

class TestBinarioHexadecimal(unittest.TestCase):
    def test17(self):
        result = binario2hexadecimal(1111011)
        self.assertEqual(result, "7B")

    def test18(self):
        result = binario2hexadecimal(111)
        self.assertEqual(result, "7")
    
    def test19(self):
        result = binario2hexadecimal(110101)
        self.assertEqual(result, "35")

    def test20(self):
        result = binario2hexadecimal(101010)
        self.assertEqual(result, "2A")

class TestBinarioOctal(unittest.TestCase):
    def test21(self):
        result = binario2octal(1111011)
        self.assertEqual(result, "173")

    def test22(self):
        result = binario2octal(11111)
        self.assertEqual(result, "37")
    
    def test23(self):
        result = binario2octal(110101)
        self.assertEqual(result, "65")

    def test24(self):
        result = binario2octal(101010)
        self.assertEqual(result, "52")

class TestHexadecimalDecimal(unittest.TestCase):
    def test25(self):
        result = hexadecimal2decimal("1A")
        self.assertEqual(result, 26)

    def test26(self):
        result = hexadecimal2decimal("45B")
        self.assertEqual(result, 1115)
    
    def test27(self):
        result = hexadecimal2decimal("68")
        self.assertEqual(result, 104)

    def test28(self):
        result = hexadecimal2decimal("F")
        self.assertEqual(result, 15)

class TestHexadecimalBinario(unittest.TestCase):
    def test29(self):
        result = hexadecimal2binario("1A")
        self.assertEqual(result, "11010")

    def test30(self):
        result = hexadecimal2binario("45B")
        self.assertEqual(result, "10001011011")
    
    def test31(self):
        result = hexadecimal2binario("68")
        self.assertEqual(result, "1101000")

    def test32(self):
        result = hexadecimal2binario("F")
        self.assertEqual(result, "1111")

class TestHexadecimalOctal(unittest.TestCase):
    def test33(self):
        result = hexadecimal2octal("1A")
        self.assertEqual(result, "32")

    def test34(self):
        result = hexadecimal2octal("45B")
        self.assertEqual(result, "2133")
    
    def test35(self):
        result = hexadecimal2octal("68")
        self.assertEqual(result, "150")

    def test36(self):
        result = hexadecimal2octal("F")
        self.assertEqual(result, "17")

class TestOctalDecimal(unittest.TestCase):
    def test37(self):
        result = octal2decimal("145")
        self.assertEqual(result, 101)

    def test38(self):
        result = octal2decimal("5")
        self.assertEqual(result, 5)
    
    def test39(self):
        result = octal2decimal("240")
        self.assertEqual(result, 160)

    def test40(self):
        result = octal2decimal("777")
        self.assertEqual(result, 511)

class TestOctalBinario(unittest.TestCase):
    def test41(self):
        result = octal2binario("145")
        self.assertEqual(result, "1100101")

    def test42(self):
        result = octal2binario("5")
        self.assertEqual(result, "101")
    
    def test43(self):
        result = octal2binario("240")
        self.assertEqual(result, "10100000")

    def test44(self):
        result = octal2binario("777")
        self.assertEqual(result, "111111111")

class TestOctalHexadecimal(unittest.TestCase):
    def test45(self):
        result = octal2hexadecimal("145")
        self.assertEqual(result, "65")

    def test46(self):
        result = octal2hexadecimal("5")
        self.assertEqual(result, "5")
    
    def test47(self):
        result = octal2hexadecimal("240")
        self.assertEqual(result, "A0")

    def test48(self):
        result = octal2hexadecimal("777")
        self.assertEqual(result, "1FF")


if __name__ == '__main__':
    unittest.main()