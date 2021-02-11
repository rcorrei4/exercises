#This line creates a string(str) variable thats receive ' Ricardo '.
name = str(' Ricardo ')
#This line prints the variable name, first with the whitespaces, name.strip
#removes all whitespaces on the right, name.lstrip removes all whitespaces
#on the left then name.strip removes all whitespaces in both sides.
print(f'\n\t{name}\n\t{name.rstrip()}\n\t{name.lstrip()}\n\t{name.strip()}')

