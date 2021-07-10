quantidade = int(input())
numeros = []
for i in range(quantidade):
	numeros.append(int(input()))

soma = []

for i in range(0, len(numeros)):
	if numeros[i] == 0:
		soma.pop()
	else:
		soma.append(numeros[i])

print(sum(soma))