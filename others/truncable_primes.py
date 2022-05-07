def truncatable(n):
	# Nao pode possuir 0
	if '0' in str(n):
		return False
	else:
		left_truncatable = True

		# Verificar se o numero continua primo removendo algarismos da esquerda para a direita
		for tamanho in range(len(str(n))):
			"""
			Converte n para string para utilizar somente o numero de acordo 
			com o tamanho depois converte para int de volta
			"""
			numero = int(str(n)[tamanho:])

			# Retorna Falso caso seja menor que 2 ja que o numeros primos sao maiores que 1
			if numero < 2:
				left_truncatable = False
				break

			# Caso o numero seja divisivel por algum numero alem de 1 e ele mesmo ele nao e primo
			for i in range(2, numero):
				if int(str(n)[tamanho:]) % i == 0:
					left_truncatable = False
					break


		right_truncatable = True

		# Verificar se o numero continua primo removendo algarismos da direita para a esquerda
		for tamanho in range(1, len(str(n))):
			"""
			Converte n para string para utilizar somente o numero de acordo 
			com o tamanho depois converte para int de volta
			"""
			numero = int(str(n)[:-tamanho])

			# Retorna Falso caso seja menor que 2 ja que os numeros primos sao maiores que 1
			if numero < 2:
				right_truncatable = False
				break

			# Caso o numero seja divisivel por algum numero alem de 1 e ele mesmo ele nao e primo
			for i in range(2, numero):
				if numero % i == 0:
					right_truncatable = False
					break

	if left_truncatable and right_truncatable:
		return 'both'
	if left_truncatable and not right_truncatable:
		return 'left'
	if not left_truncatable and right_truncatable:
		return 'right'

	return False