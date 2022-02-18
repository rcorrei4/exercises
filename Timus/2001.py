all_weights = []

for i in range(3):
	weights = [int(x) for x in input().split(" ")]
	all_weights.append(weights[0])
	all_weights.append(weights[1])

print(all_weights[0] - all_weights[4], all_weights[1] - all_weights[3])