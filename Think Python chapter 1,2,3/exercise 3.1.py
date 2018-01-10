Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'chapter 3 exercise code'
'chapter 3 exercise code'
>>> "exercise 1 Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get. "
'exercise 1 Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get. '
>>> '将程序的最后一行移动到最顶层，这样函数在定义之前就要执行。运行这段程序，看看能得到什么错误信息'
'将程序的最后一行移动到最顶层，这样函数在定义之前就要执行。运行这段程序，看看能得到什么错误信息'
>>> def print_ss( ):
	print "I' m a new programer, and I' m OK"
	
SyntaxError: Missing parentheses in call to 'print'
>>> def print_ss( ):
	print " I' m a new programer, and I' m OK. "
	
SyntaxError: Missing parentheses in call to 'print'
>>> def print_ss( ):
	print (" I' m a new programer, and I' m OK. ")

	
>>> print print_ss
SyntaxError: Missing parentheses in call to 'print'
>>> print (print_ss)
<function print_ss at 0x008985D0>
>>> type (print_ss)
<class 'function'>
>>> print_ss
<function print_ss at 0x008985D0>
>>> print_ss()
 I' m a new programer, and I' m OK. 
>>> def repeat_ss():
	print_ss()
	print_ss()

	
>>> repeat_ss()
 I' m a new programer, and I' m OK. 
 I' m a new programer, and I' m OK. 
>>> 
