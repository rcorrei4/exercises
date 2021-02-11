age = int(input('Enter the person age: '))

if age < 2:
    print('This person is a baby!')
elif age < 4:
    print('This person is a toddler!')
elif age < 13:
    print('This person is kid!')
elif age < 20:
    print('This person is a teenager!')
elif age < 65:
    print('This person is a adult!')
else:
    print('This person is a elder!')
