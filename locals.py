"""locals.py
examples of local variables"""

A = 'This is the text message from main'

def test1():
    print('In test1.')
    print(A)
    print('Leaving test1.')

def test2():
    print('In test2.')
    A = "This is test2's text message."
    print(A)
    print('Leaving test2.')

def test3():
    print('In test3.')
    print(A)
    A = "This is test3's text message."
    print('Leaving test3.')
    

test1()
print('Back in main')
print(A)
test2()
print('Back in main')
print(A)
test3()
