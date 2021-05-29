from ctypes import *
import os


def test(value,expect):
	try:
		assert value == expect
	except AssertionError:
		return"Invalid values, expect number is different\nValue = {:d} Expect = {:d}".format(value,expect)
	return "OK. Value = {:d} Expect = {:d}".format(value,expect)

lib = cdll.LoadLibrary(os.path.abspath("lib.so"))

Polindrom=121
isPolindrom=lib.isPolindrom(Polindrom)
print('Test 1')
print(test(isPolindrom,False))

a=14
b=2
checkDel=lib.checkDel(a,b)
print('Test 2')
print(test(checkDel,True))

theBiggest=6
theBiggestTest=lib.theBiggest(4,2,6)
print('Test 3')
print(test(theBiggest,theBiggestTest))

theBiggest2=1
theBiggestTest2=lib.theBiggest(4,1,6)
print('Test 4')
print(test(theBiggest2,theBiggestTest2))