n_premiados = int(input())
tamanhos_solicitados = [int(i) for i in input().split()]
n_pequenas = int(input())
n_medias = int(input())

if tamanhos_solicitados.count(1) > n_pequenas or tamanhos_solicitados.count(2) > n_medias:
	print("N")
else:
	print("S")