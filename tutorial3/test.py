global num
num = 0
print('import test.py, num address is {}'.format(id(num)))
def increment():      
    global num    
    print('call by main.py, before increment,  num address is {}'.format(id(num)))
    num += 1
    print('call by main.py, after increment , num address is {}'.format(id(num)))
    
