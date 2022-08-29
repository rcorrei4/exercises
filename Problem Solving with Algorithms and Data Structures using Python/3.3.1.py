import random

randomlist = []
for i in range(0,50):
	n = random.randint(1,50)
	randomlist.append(n)

min_value = randomlist[0]
for i in randomlist:
	for j in randomlist:
		if i < j and i < min_value:
			min_value = i

print(min_value, min(randomlist))

for i in randomlist:
	if i < min_value:
		min_value = i

print(min_value, min(randomlist))