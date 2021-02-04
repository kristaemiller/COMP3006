
#Krista Miller
# Data Science 2, Project 02
# the default characters are 'Aaaaabbcdrr!'
import count as c
import unittest
import sys

all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_letters_lower = 'abcdefghijklmnopqrstuvwxyz'
path = r"test.txt"

class TestCountMethods(unittest.TestCase):

	def setUp(self):
		#setUp is used to assert equal with the output of the dictionary from count.py
		self.d = {'a': 5, 'b': 2, 'c': 1, 'd': 1, 'r': 2}
		self.dc = {'a': 4, 'b': 2, 'c': 1, 'd': 1, 'r': 2, 'A': 1}
		self.dl = {'a': 5, 'b': 2, 'c': 1}
		self.dcl = {'a': 4, 'b': 2, 'c': 1, 'A': 1}

		self.dz = {}
		for i in all_letters_lower:
			self.dz[i] = 0
		self.dz['a'] = 5
		self.dz['b'] = 2
		self.dz['c'] = 1
		self.dz['d'] = 1
		self.dz['r'] = 2

		self.dcz = {}
		for i in all_letters:
			self.dcz[i] = 0
		self.dcz['a'] = 4
		self.dcz['b'] = 2
		self.dcz['c'] = 1
		self.dcz['d'] = 1
		self.dcz['r'] = 2
		self.dcz['A'] = 1

		self.dlz = {'a': 5, 'b': 2, 'c': 1, 'z': 0}
		self.dclz = {'a': 4, 'b': 2, 'c': 1, 'z': 0, 'A': 1}

	def test_null(self): #no flags
		sys.argv = ['count.py', path]
		self.assertEqual(c.main(), self.d)

	def test_c(self): #-c flag only
		sys.argv = ['count.py', '-c', path]
		self.assertEqual(c.main(), self.dc)

	def test_l(self): #-l flag only
		sys.argv = ['count.py', '-l', 'Aabc', path]
		self.assertEqual(c.main(), self.dl)

	def test_z(self): #-z flag only
		sys.argv = ['count.py', '-z', path]
		self.assertEqual(c.main(), self.dz)

	def test_cl(self): #-c and -l flags
		sys.argv = ['count.py', '-c', '-l', 'Aabc', path]
		self.assertEqual(c.main(), self.dcl)

	def test_cz(self): #-c and -z flags
		sys.argv = ['count.py', '-c', '-z', path]
		self.assertEqual(c.main(), self.dcz)

	def test_lz(self): #-l and -z flags
		sys.argv = ['count.py', '-l', 'Aabcz', '-z', path]
		self.assertEqual(c.main(), self.dlz)

	def test_clz(self): #-c, -l, and -z flags
		sys.argv = ['count.py', '-c', '-l', 'Aabcz', '-z', path]
		self.assertEqual(c.main(), self.dclz)

if __name__ == '__main__': #if we run the module directly, then run the code within this conditional
	unittest.main()

#references:
#https://docs.python.org/3/library/unittest.html
#https://stackoverflow.com/questions/23369588/python-unit-testing-methods-inside-of-classes
