Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## chapter 3 exercise 3.5
>>> ## use the character ‘+’, '-' print the diagram
>>> print('+'),    # test code
+
(None,)
>>> print('+'),print('-')
+
-
(None, None)
>>> print('+', '-') ###test code
+ -
>>> def print_orig(a, b)
SyntaxError: invalid syntax
>>> def print_orig(a, b):
	return (a+b*4)*2+a+'\n'

>>> def print_x1();
SyntaxError: invalid syntax
>>> def print_x1():
	return print_orig('+','-')

>>> def print_x2():
	return print_orig('|', ' ')

>>> def print_grid():
	a=print_orig(print_x1(), print_x2())
	print(a)

	
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print_grid()
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+


>>> ### 输出有些问题了，相乘的地方没有对应上
