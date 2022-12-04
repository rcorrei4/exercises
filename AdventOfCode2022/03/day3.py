input_data = open('input.txt', 'r').read().split('\n')

sum_priority = 0
for line in input_data:
	compartment1 = line[:int(len(line)/2)]
	compartment2 = line[int(len(line)/2):]

	for i in range(len(compartment1)):
		if compartment1[i] in compartment2:
			if compartment1[i].islower():
				sum_priority += ord(compartment1[i]) - 96
			else:
				sum_priority += ord(compartment1[i]) - 38
			break
			

print(sum_priority)

sum_priority_group = 0
for i in range(0, len(input_data), 3):
	for j in range(len(input_data[i])):
		if input_data[i][j] in input_data[i+1] and input_data[i][j] in input_data[i+2]:
			if input_data[i][j].islower():
				sum_priority_group += ord(input_data[i][j]) - 96
			else:
				sum_priority_group += ord(input_data[i][j]) - 38
			break

print(sum_priority_group)