Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add_one(a_number):
	print(a_number)

	
>>> add_one
<function add_one at 0x0000021459F6C1E0>
>>> add_one:
	
SyntaxError: invalid syntax
>>> add_one():
	
SyntaxError: invalid syntax
>>> add_one(1)
1
>>> add_one(hdrtykljhgufkjytuhliu):
	
SyntaxError: invalid syntax
>>> add_one('hdrtykljhgufkjytuhliu'):
	
SyntaxError: invalid syntax
>>> def add_one('rfdjtygjrdesrjftkyfrdtfygfktdrjtfkyjrdh'):
	
SyntaxError: invalid syntax
>>> add_one(6587865768576858567685658656585686587685687567856577655768)
6587865768576858567685658656585686587685687567856577655768
>>> 
>>> def print_two_numbers(abnm):
	print(abnm)

	
>>> print_two_numbers(567,789)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print_two_numbers(567,789)
TypeError: print_two_numbers() takes 1 positional argument but 2 were given
>>> 
>>> 
>>> def print_two_numbers(abnm,ghjk):
	print("abnm= "+', ghjk='+str(b))

	
>>> print_two_numbers(567,927)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print_two_numbers(567,927)
  File "<pyshell#20>", line 2, in print_two_numbers
    print("abnm= "+', ghjk='+str(b))
NameError: name 'b' is not defined
>>> def print_two_numbers(abnm,ghjk):
	print("abnm= "+', ghjk='+str(ghjk))

	
>>> print_two_numbers(567,927)
abnm= , ghjk=927
>>> def print_two_numbers(abnm,ghjk):
	print("abnm = "+str(abnm)', ghjk ='+str(ghjk))
	
SyntaxError: invalid syntax
>>> def print_two_numbers(abnm,ghjk):
	print("abnm = "+str(abnm)', ghjk='+str(ghjk))
	
SyntaxError: invalid syntax
>>> def print_two_numbers(abnm,ghjk):
	print("abnm = "+str(abnm)+', ghjk ='+str(ghjk))

	
>>> print_two_numbers(567,927)
abnm = 567, ghjk =927
>>> def print_two_numbers(abnm,ghjk):
	print("abnm = "+str(abnm)+', ghjk = '+str(ghjk))

	
>>> print_two_numbers(567,927)
abnm = 567, ghjk = 927
>>> def add_one(a,b,display=True):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))

		
>>> add_one(1,2)
a= 1
b= 2
>>> add_one(1,2,False)
>>> def add_one(a,b,display=True):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif
	
SyntaxError: invalid syntax
>>> def add_one(a,b,display=True):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif:
		
SyntaxError: invalid syntax
>>> def add_one(a,b,display=True):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	else:
		print(display)

		
>>> add_one(45,12)
a= 45
b= 12
>>> add_one(45,12,False)
False
>>> def add_one(display=True,a,b):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	else:
		print(display)
		
SyntaxError: non-default argument follows default argument
>>> def add_one(a,b,display=True, lulu = 0):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif lulu == 0:
		print (lulu)		
	else:
		print(display)

		
>>> add_one (1,2,False)
0
>>> add_one (1,2,False,1)
False
>>> add_one (1,2,False,0)
0
>>> def add_one(a,b,display=True, ghjt = 0):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif lulu == 0:
		print (ghjt)
	else:
		print(display)

		
>>> def add_one(a,b,display=True, ghjt = 0):
	if display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif ghjt == 0:
		print (ghjt)
	else:
		print(display)

		
>>> def add_one(a,b,display=True, ghjt = 0):
	if display = True:
		print("a= "+str(a))
		print("b= "+str(b))
	elif ghjt == 0:
		print (ghjt)
	else:
		print(display)
		
SyntaxError: invalid syntax
>>> def add_one(a,b,display=True, ghjt = 0):
	if display == True:
		print("a= "+str(a))
		print("b= "+str(b))
	elif ghjt == 0:
		print (ghjt)
	else:
		print(display)

		
>>> def add_one(a,b,display=True, ghjt = 0):
	if display == False:
		print("a= "+str(a))
		print("b= "+str(b))
	elif ghjt == 0:
		print (ghjt)
	else:
		print(display)

		
>>> add_one(1,2, False)
a= 1
b= 2
>>> def add_one(a,b,display=True, ghjt = 0):
	if !display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif ghjt == 0:
		print (ghjt)
	else:
		print(display)
		
SyntaxError: invalid syntax
>>> def add_one(a,b,display=True, ghjt = 0):
	if not display:
		print("a= "+str(a))
		print("b= "+str(b))
	elif ghjt == 0:
		print (ghjt)
	else:
		print(display)

		
>>> add_one (1,2,False)
a= 1
b= 2
>>> add_one (1,2,False,0)
a= 1
b= 2
>>> def add_one(a,b,display=True, ghjt = 0):
	if not display:
		print("a= "+str(a))
		print("b= "+str(b))
	if ghjt == 0:
		print (ghjt)
	else:
		print(display)

		
>>> add_one (1,2,False,0)
a= 1
b= 2
0
>>> def add_one(a_number):
	return a_number+1

>>> add_one(67)
68
>>> add_one(hello)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    add_one(hello)
NameError: name 'hello' is not defined
>>> retval = add_one(67)
>>> retval
68
>>> def add_one(a_number):
	print (a_number+1)

	
>>> add_one(3)
4
>>> retval = add_one(3)
4
>>> retval
>>> add_one("heeelo")
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    add_one("heeelo")
  File "<pyshell#82>", line 2, in add_one
    print (a_number+1)
TypeError: can only concatenate str (not "int") to str
>>> def add_one(a_number):
	print (a_number+str(1))

	
>>> add_one("heeelo")
heeelo1
>>> def add_one(a_number):
	print (a_number+str(False))

	
>>> add_one("heeelo")
heeeloFalse
>>> def add_one(a_number):
	print (a_number+False)

	
>>> add_one("heeelo")
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    add_one("heeelo")
  File "<pyshell#94>", line 2, in add_one
    print (a_number+False)
TypeError: can only concatenate str (not "bool") to str
>>> add_one(True)
1
>>> print(True+True)
2
>>> print(True+True+True)
3
>>> print(True+True+True+789)
792
>>> def add_one(a_number):
	print (a_number+1)

	
>>> retval = add_one(2)
3
>>> retval
>>> print(retval)
None
>>> def add_one(a_number):
	return (a_number+1)

>>> retval = add_one(2)
>>> retval
3
>>> def add_one(a_number):
	if a_number == 10:
		return(a_number+1)
	elif a_number ==20:
		return(a_number+2)

	
>>> add_one(21)
>>> retval
3
>>> retval = add_one(21)
>>> retval
>>> print(retval)
None
>>> retval = add_one(20)
>>> retval
22
>>> def calculater ( num1, num2, operation):
	if operation == "sum":
		print(add_one(10))

		
>>> calcdef calculater ( num1, num2, operation):
	if operation == "add1":
		print(add_one(10))
		
SyntaxError: invalid syntax
>>> calcdef calculater ( num1, num2, operation):
	if operation == "addon":
		print(add_one(10))
		
SyntaxError: invalid syntax
>>> def calculater ( num1, num2, operation):
	if operation == "add1":
		print(add_one(10))

		
>>> calculater(1,2,"add1")
11
>>> 
