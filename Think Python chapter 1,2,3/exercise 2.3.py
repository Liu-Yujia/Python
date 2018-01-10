Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:30:08) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'chapter 2 exercise 2.3 Practice using the Python interpreter as a calculator: 1. The volume of a sphere with radius r is 4 3pr3. What is the volume of a sphere with radius 5?  Hint: 392.7 is wrong! '
'chapter 2 exercise 2.3 Practice using the Python interpreter as a calculator: 1. The volume of a sphere with radius r is 4 3pr3. What is the volume of a sphere with radius 5?  Hint: 392.7 is wrong! '
>>> '2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?'
'2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?'
>>> 'If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?'
'If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?'
>>> 
'chapter 2 exercise 2.3 Practice using the Python interpreter as a calculator: 1. The volume of a sphere with radius r is 4 3pr3. What is the volume of a sphere with radius 5?  Hint: 392.7 is wrong! '
'chapter 2 exercise 2.3 Practice using the Python interpreter as a calculator: 1. The volume of a sphere with radius r is 4 3pr3. What is the volume of a sphere with radius 5?  Hint: 392.7 is wrong! '
>>> r=5
>>> pi=3.14
>>> v=4*pi*(r**3)/3
>>> v
523.3333333333334
>>>  '2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?'
 
SyntaxError: unexpected indent
>>> '2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?'

 
'2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?'
>>> '计算折扣题，同时算出复印六十本书的总价，复印一本花3美元，之后每份0.75美元’
SyntaxError: EOL while scanning string literal
>>> '计算折扣题，同时算出复印六十本书的总价，复印一本花3美元，之后每份0.75美元'
'计算折扣题，同时算出复印六十本书的总价，复印一本花3美元，之后每份0.75美元'
>>> bookp=24.95
>>> fristcopy=3
>>> addcopy=0.75
>>> totalcosr=bookp*0.4+fristcopy+addcopy*59
>>> totalcost
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    totalcost
NameError: name 'totalcost' is not defined
>>> totalcosr
57.230000000000004
>>> 
