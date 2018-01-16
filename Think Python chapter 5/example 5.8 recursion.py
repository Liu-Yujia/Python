Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## example 5.8 recursion
>>> def countdown():
	if n<0
	
SyntaxError: invalid syntax
>>> def countdown():
	if n<0:
		print ('blastooff ')
	else:
		print ('n')
		countdown(n-1)

		
>>> countdown(5)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    countdown(5)
TypeError: countdown() takes 0 positional arguments but 1 was given
>>>  def countdown(n):
	if n<0:
		print ('blastooff ')
	else:
		print ('n')
		countdown(n-1)

SyntaxError: unexpected indent
>>> def countdown(n):
	if n<0:
		print ('blastooff ')
	else:
		print ('n')
		countdown(n-1)

		
>>> countdown (5)
n
n
n
n
n
n
blastooff 
>>> def countdown(n):
	if n<0:
		print ('blastooff ')
	else:
		print (n)
		countdown(n-1)

		
>>> countdown (5)
5
4
3
2
1
0
blastooff 
>>> 
