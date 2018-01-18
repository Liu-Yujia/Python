### the question 1 is finished here, you can check the result us functon check_format()
def check_fermat(a, b, c, n):
    if n > 2:
      if a**n + b**n == c**n :  
         return "No, that doesn't work"
      else :
         return "Holy smokes, Fermat was wrong"

###  the question 2 solution
def fermat_input():
  a = int(raw_input("enter a varible a", ))
  b = int(raw_input("enter a varible b"))
  c = int(raw_input("enter a varible c"))
  n = int(raw_input("enter a varible n"))
  print (check_fermat(a, b, c, n))


