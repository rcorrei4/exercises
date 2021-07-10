with open('/home/ricardo/Documents/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())