def insertion_sort(A): 
	for j in range(len(A)):
		key = A[j]
		i = j-1

		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key

	return A

def insertion_sort_decreasing(A):
	for j in range(len(A)):
		key = A[j]
		i = j-1

		while i >= 0 and A[i] < key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key

	return A

print(insertion_sort([5, 2, 4, 6, 1, 3]))
print(insertion_sort_decreasing([5, 2, 4, 6, 1, 3]))