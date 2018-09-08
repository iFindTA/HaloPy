#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

import functools

print('hello, world!')

i = 1
s = str(i) + 'shame on you'
print(s)

print(type(i))

list1 = ['sss',i,s]
print(list1[1])

#dictionary

user={'liangshui':'ssss', 'dddd':'dddd'}
print(user)

user.clear()
print(type(user))

#创建set需要list初始化
set1 = set([123,456,789])
print(set1)

set1=set('hello')
set2=set(['p','y','t','h','o','n'])
print(set1)
print(set2)

set3 = set1 & set2
print(set3)

count=1
sum=0
while count<=100:
	sum=sum+count
	count+=1
else:
	print(count)
print(sum)

for n in range(10,20):
	for i in range(2,n):
		if n%i == 0:
			j=n/i
			print('%d 是一个合数' % n)
			break
	else:
		print('%d是一个质数' % n)


#九九乘法表
for i in range(1,10):
	for j in range(1,i+1):
		print('{}x{}={}\t'.format(j, i, i*j), end='')

	print()


def sum(n1, n2):
	"两数之和"
	if not (isinstance (n1,(int,float)) and isinstance (n2,(int,float))):
		raise TypeError('参数类型错误！')
	return n1+n2
def division(n1, n2):
	#求商与余数
	a = n1 % n2
	b = (n1-a) / n2
	return b, a

#默认参数值
_nil_value = object()
def testDefault(a, b=_nil_value):
	if b is _nil_value:
		print('b默认没有赋值')
	return

print(sum(5,6))
tulpe1 = division(9, 4)
print(tulpe1)

def changelist(l):
	l.append(1000)

b=[1,2,3,4,5]
changelist(b)
print(b)


def power(x):
	return x*x
#默认参数必须指向不可变对象！
def power1(x, n=2):
	s=1
	while n > 0:
		n = n - 1
		s = s * x
	return s

#可变参数 接收的是tulpe
def calculate(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum
nums = [1, 2, 3, 4, 5, 6]
tulp2 = (1, 2, 3, 4, 5, 6, 7)
print(calculate(*nums), calculate(*tulp2))

#关键字参数 接收的是dict
def person(name, age, **kw):
	print('name: %s' % name)
	print(kw)

person('nanhu', 29, city='kaifeng', zone='tongxu')
kw = {'city':'nanyang', 'zone':'xiangfu'}
person('jiaju', 30, **kw)

"""
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，
参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
"""
def testParams(a, b=1, *args, **kw):
	pass

for key in kw:
	print(key, end = "  ")
	print('\n')


#递归 需要防止栈溢出:尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

def fact1(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1, num*product)

print(fact(5))


#生成式
print([x * x for x in range(0, 10)])
print([m + n for m in 'ABC' for n in 'XYZ'])
print('\n'.join([' '.join('%d x %d = %d' % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)]))
#生成器
gen=(x * x for x in range(1,11))
print(gen)
for x in gen:
	print(x)


#装饰器：返回函数的高介函数
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2018-8-9')

print(now.__name__)#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
now()
