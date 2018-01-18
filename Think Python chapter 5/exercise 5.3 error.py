Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## chapter 5 exercise 5.3
>>> ## Fermat’s Last Theorem says that there are no positive integers a, b, and c such that an + bn = cn  for any values of n greater than 2.
>>> ### 1. Write a function named check_fermat that takes four parameters—a, b, c and n—and that checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
>>> #### a^n + b^n = c^n
>>> #### the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”
>>> def check_fermat(a, b, c, n ):
	 a^n + b^n = c^n
	 
SyntaxError: can't assign to operator
>>> def check_fermat(a, b, c, n ):
	      a^n + b^n = c^n
	      
SyntaxError: can't assign to operator
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n x2= c^n
	      
SyntaxError: invalid syntax
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1=x2:
		      
SyntaxError: invalid syntax
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    else if x1 == x2 and n<=2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    else if x1 == x2 and n<2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    else
                    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    else:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1==x2 and n<=2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1==x2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2:
		      print("Holy smokes, Fermat was wrong!")
                    else:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 :
		      print("Holy smokes, Fermat was wrong!")
                    elif x1!==x2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1==x2 :
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif  x1!==x2 :
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1==x2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1==x2
                    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1 !== x2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1 !== x2 :
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1 > x2:
			    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1 !== x2 ;
                    
SyntaxError: unindent does not match any outer indentation level
>>> def check_fermat(a, b, c, n ):
	      x1=a^n + b^n
	      x2= c^n
	      if x1==x2 and n>2:
		      print("Holy smokes, Fermat was wrong!")
                    elif x1 !== x2 :
			    
SyntaxError: unindent does not match any outer indentation level
>>> 
