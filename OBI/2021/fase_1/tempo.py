from re import search

n_registros = int(input())
registros = []
for linha in range(n_registros):
	registros.append(str(input()).replace(" ", ""))

resposta_amigo = []

for i in registros:
	if search("R", i):
		if i not in resposta_amigo:
			resposta_amigo.append(i)

for i in resposta_amigo:
	count = 0
	pos_resposta = registros.index(i)
	for j in registros[pos_resposta:]:
		pos_registro = registros.index(j)
		try:
			if search("T", registros[pos_registro+1]):
				print(registros[pos_registro+1])
		except IndexError:
			continue

		try:
			if search("T", registros[pos_registro-1]):
				print(registros[pos_registro-1])
		except IndexError:
			contiue