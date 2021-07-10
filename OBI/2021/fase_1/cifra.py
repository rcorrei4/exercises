palavra = str(input())
alfabeto_raw = "abcdefghijklmnopqrstuvxz"
alfabeto = [x for x in alfabeto_raw]

vogais = "aeiou"

resultado = ""

def distancia_vogal(letra):
	distancia_vogais = []

	for i in vogais:
		distancia_vogais.append(abs(alfabeto.index(i) - alfabeto.index(letra)))

	for j in distancia_vogais:
		if distancia_vogais.count(j) > 1:
			return -j

	return min(distancia_vogais)

def distancia_consoante(letra):
	pos = alfabeto.index(letra)
	for i in alfabeto[pos+1:]:
		if i not in vogais:
			return i

for i in palavra:
	letra_index = alfabeto.index(i)

	if i in vogais:
		resultado += i

	elif i in "xyz":
		resultado = resultado + i
		resultado += alfabeto[letra_index-distancia_vogal(i)]
		if i == "z":
			resultado += "z"
		else:
			resultado += distancia_consoante(i)

	else:
		resultado = resultado + i
		resultado += alfabeto[letra_index+distancia_vogal(i)]
		if i == "z":
			resultado += "z"
		else:
			resultado += distancia_consoante(i)

print(resultado)