message = '\nEnter you age to see the ticket prize.'

while True:
    age = int(input(message))

    if age < 3:
        print('Your ticket is free!')
    elif age <= 12:
        print('Your ticket is $10.')
    elif age > 12:
        print('Your ticket is $15.')
