n_tamanho = int(input())
numeros = [int(i) for i in input().split()]
res = []

for i in range(0, len(numeros)):
	res[i] += 1
	for j in range(len(numeros)):
		if numeros[0] == numeros[1]:
			pass
		else:
			res[i] += 1


