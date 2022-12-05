input_data = open('04/input.txt', 'r').read().split('\n')

count = 0
for pairs in input_data:
	pair = [line.split('-') for line in pairs.split(',')]

	section1 = [x for x in range(int(pair[0][0]), int(pair[0][1])+1)]
	section2 = [x for x in range(int(pair[1][0]), int(pair[1][1])+1)]

	if len(section1) > len(section2):
		laping = [x for x in section2 if x in section1]
		if laping == section2:
			count += 1
	else:
		laping = [x for x in section1 if x in section2]
		if laping == section1:
			count += 1

print(count)

count = 0
for pairs in input_data:
	pair = [line.split('-') for line in pairs.split(',')]

	section1 = [x for x in range(int(pair[0][0]), int(pair[0][1])+1)]
	section2 = [x for x in range(int(pair[1][0]), int(pair[1][1])+1)]

	laping = [x for x in section1 if x in section2]
	if laping:
		count += 1

print(count)