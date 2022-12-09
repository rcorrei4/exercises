input_data = open('input.txt', 'r').read().split('\n')

for i in range(len(input_data)):
	input_data[i] = [int(x) for x in input_data[i]]

count = 0
for i in range(len(input_data)):
	if input_data[i] == input_data[-1] or input_data[i] == input_data[0]:
		count += len(input_data[i])
	else:
		count += 2
		for j in range(1, len(input_data[i])-1):
			if input_data[i][j] > max(input_data[i][:j]) or input_data[i][j] > max(input_data[i][j+1:]):
				count += 1
			else:
				columm = [input_data[k][j] for k in range(len(input_data))]
				if input_data[i][j] > max(columm[:i]) or input_data[i][j] > max(columm[i+1:], default=input_data[i][j]):
					count += 1

print(count)

def count_tree(trees, tree):
	if not trees:
		return 1
	tree_seq = []
	tree_seq.append(trees[0])
	for i in range(1, len(trees)):
		if tree_seq[-1] >= tree:
			break
		else:
			tree_seq.append(trees[i])
	return len(tree_seq)

max_tree_views = 0

for i in range(len(input_data)):
	for j in range(len(input_data[i])):
		columm = [input_data[k][j] for k in range(len(input_data))]
		tree_views = 1
		tree_views *= count_tree(list(reversed(columm[:i])), input_data[i][j])
		tree_views *= count_tree(list(reversed(input_data[i][:j])), input_data[i][j])
		tree_views *= count_tree(columm[i+1:], input_data[i][j])
		tree_views *= count_tree(input_data[i][j+1:], input_data[i][j])
		if tree_views > max_tree_views:
			max_tree_views = tree_views
		tree_views = 1

print(max_tree_views)