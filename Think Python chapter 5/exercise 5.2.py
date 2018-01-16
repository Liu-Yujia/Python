Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ### Write a function called do_n that takes a function object and a number, n, as arguments, and that calls the given function n times.
>>> ### chapter 5 exercise 5.2
>>> def do_n (s, n ):
	s= print (n )
	if n <=0
	
SyntaxError: invalid syntax
>>> def do_n (s, n ):
	s= print (n )
	if n <=0:
		return 0
	else
	
SyntaxError: invalid syntax
>>> def do_n (s, n ):
	s= print (n )
	if n <=0:
		return 0
	else:
		do_n (s, n-1 )

		
>>> do_n( s, 5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    do_n( s, 5)
NameError: name 's' is not defined
>>> do_n( 6, 5)
5
4
3
2
1
0
>>> 
