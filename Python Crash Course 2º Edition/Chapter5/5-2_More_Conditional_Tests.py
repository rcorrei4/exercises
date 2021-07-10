#Equality and Inequality
book = 'good'

print("\nIs book == 'good'?")
print(book == 'good')

print("Is book == 'bad'?")
print(book == 'bad')

#Test with lower() function
fast_car = 'Ferrari'

print("\nIs fast_car == 'ferrari'?")
print(fast_car == 'ferrari')

print("Is fast_car.title == 'Ferrari'?")
print(fast_car.lower() == 'ferrari')

#Numerical Equality and Inequality
lucky_number = 2

print('\nIs lucky_number == 10?')
print(lucky_number == 10)

print('Is lucky number == 2?')
print(lucky_number == 2)

#Numerical Greater than and Less than
number = 10

print('\nIs number > 100?')
print(number > 100)

print('Is number < 100?')
print(number < 100)

#Greater than or equal to
number = 90

print('\nIs number >= 80?')
print(number >= 80)

print('Is number >= 100?')
print(number >= 100)

#Less than or equal to
number = 90

print('\nIs number <= 70?')
print(number <= 70)

print('Is number <= 100')
print(number <= 100)

#Test using _and_
num1 = 20
num2 = 10

print('\nIs num1 >= 90 and num2 > 90?')
print((num1 >=90) and (num2 > 90))

print('Is num1 < 90 and num2 <= 90?')
print((num1 < 90) and (num2 <=90))

#Test using _or_
num1 = 50
num2 = 90

print('\nIs num1 > 40 or num2 < 10?')
print((num1 > 40) or (num2 <= 10))

print('Is num1 < 40 or num2 < 80?')
print((num1 < 40) or (num2 < 80))

#Test whether an item is in a list
list = ['computer', 'smartphone', 'radio']
print('\n'+ str(list))

print("\nIs 'tablet' in list?")
print('tablet' in list)

print("Is 'radio' in list?")
print('radio' in list)

#Test whether an item is not in a list

print("\nIs 'tablet' not in list?")
print('tablet' not in list)

print("Is 'radio' not in list?")
print('radio' not in list)