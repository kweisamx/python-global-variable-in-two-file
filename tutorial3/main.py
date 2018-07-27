from test import increment, num

print('before increment num in main.py, num address is {}'.format(id(num)))
increment()
print('final num value {} and address {}'.format(num, id(num)))
