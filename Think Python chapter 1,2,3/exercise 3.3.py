Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'chapter 3, exercise 3.3'
'chapter 3, exercise 3.3'
>>> 'Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.'
SyntaxError: invalid syntax
>>> 'Python provides a built-in function called len that returns the length of a string, so the value of len (allen) is 5. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.'
'Python provides a built-in function called len that returns the length of a string, so the value of len (allen) is 5. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.'
>>> def right_justify()
SyntaxError: invalid syntax
>>> def right_justify( )
SyntaxError: invalid syntax
>>> def right_justify('allen'):
	
SyntaxError: invalid syntax
>>> def right_justify(allen):
	x=len(allen)

	
>>> right_justify(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    right_justify(x)
NameError: name 'x' is not defined
>>> def right_justify(s):
	a=len(s)
	b=70-a
	print(b*' '+s)

	
>>> right_justify(allen)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    right_justify(allen)
NameError: name 'allen' is not defined

>>> right_justify('allen')
                                                                 allen
>>> #让单词的最后一个字符放到70这个位置上，就要想办法在前面放70-len(s)个空格
>>> 
