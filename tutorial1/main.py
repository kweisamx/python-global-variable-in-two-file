num = 1
def increment():
    global num
    num +=1

if __name__ == '__main__':
    print('num before, {}'.format(num))
    increment()
    print('num after increment, {}'.format(num))
