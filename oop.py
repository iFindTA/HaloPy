#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import sys
import logging
from enum import Enum

print(sys.path)

__author__ = 'nanhujiaju@gmail.com'
logging.basicConfig(level=logging.INFO)

class Test(object):
	"""docstring for Test"""
	#类属性
	clsProperty = 'sssss'
	__slots__ = ('name', 'age') #限制该class实例能添加的属性,仅对当前类实例起作用，对继承的子类是不起作用的
	def prt(self):
		print(self)
		print(self.__class__)

	@classmethod
	def clsMethod(self):
		print('call class method')

	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, value):
		pass


t = Test()
t.prt()
t.name = 'test'
print(t.name)
#t.newage = 'ss'

#print(dir(str))
print(hasattr(t, 'x'))

Test.clsMethod()
print(Test.clsProperty)




logging.info('test')
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value())

@unique
class Gender(Enum):
	"""docstring for Gender"""
	Male = 1
	Female = 0

		
