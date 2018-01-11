Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  #A function object is a value you can assign to a variable or pass as an argument. For
#example, do_twice is a function that takes a function object as an argument and calls it twice:
#def do_twice(f):
#   f()
#   f()
# Here’s an example that uses do_twice to call a function named print_spam twice.
#  def print_spam():
#  print 'spam'
#  do_twice(print_spam)
#  1. Type this example into a script and test it.
#   2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
#   function twice, passing the value as an argument.
#   3. Write a more general version of print_spam, called print_twice, that takes a string as a
#    parameter and prints it twice.
#    4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
#   5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
>>> def print_spam():
	print('spam')

	
>>> def do_twice(f):
	f()
	f()

	
>>> do_twice(spam)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    do_twice(spam)
NameError: name 'spam' is not defined
>>> do_twice('spam')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    do_twice('spam')
  File "<pyshell#7>", line 2, in do_twice
    f()
TypeError: 'str' object is not callable
>>> do_twice(print_spam)
spam
spam
>>> #the subquestion 2
>>> def do_twice(print_spam, s):
	sprint_spam(s)

	
>>> def print_spam(a):
	print('a')
	print('a')

	
>>> do_twice(print_spam, spam)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    do_twice(print_spam, spam)
NameError: name 'spam' is not defined
>>> #dam I got the wrong answer again
>>> def do_twicie(f, s):
	f(s)
	f(s)

	
>>> def print_twice(s):
	print(s)
	print(s)

	
>>> do_twice(f, s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    do_twice(f, s)
NameError: name 'f' is not defined
>>>  def print_twice(s):
	 
SyntaxError: unexpected indent
>>>  def print_twice(s):
	 
SyntaxError: unexpected indent
>>> def print_twice(s)：
SyntaxError: invalid character in identifier
>>> #many errors occours when you type the code
>>> def print_twice(s):
	print('s')
	print('s')

	
>>> do_twice(f, 's')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    do_twice(f, 's')
NameError: name 'f' is not defined
>>> do_twice(f, s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    do_twice(f, s)
NameError: name 'f' is not defined
>>> do_twice(print_twice, 's')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    do_twice(print_twice, 's')
  File "<pyshell#14>", line 2, in do_twice
    sprint_spam(s)
NameError: name 'sprint_spam' is not defined
>>> do_twice(print_twice, s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    do_twice(print_twice, s)
NameError: name 's' is not defined
>>> 
