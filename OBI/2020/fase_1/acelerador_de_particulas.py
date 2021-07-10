d = int(input())
d -= 3
resto = d % 8

if resto == 3:
	print(1)
elif resto == 4:
	print(2)
else:
	print(3)