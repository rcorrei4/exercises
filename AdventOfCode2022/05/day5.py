input_data = open('05/input.txt', 'r').read().split('\n')

def create_list(data):
	global crates
	line = [data[i:i+4] for i in range(0, len(data), 4)]

	if not crates:
		crates = [[] for _ in range(len(line))]

	for i in range(len(line)):
		if line[i].strip() and not line[i].strip().isnumeric():
			crates[i].insert(0, line[i].strip().replace('[', '').replace(']', ''))

crates = []

for data in input_data:
	if data:
		if data[0] != 'm':
			create_list(data)
		elif data[0] == 'm':
			data = data.split()
			for i in range(int(data[1])):
				crates[int(data[-1])-1].append(crates[int(data[3])-1].pop())

top_crates = ""
for crate in crates:
	top_crates += crate[-1]

print(top_crates)

crates = []

for data in input_data:
	if data:
		if data[0] != 'm':
			create_list(data)
		elif data[0] == 'm':
			data = data.split()

			crates[int(data[-1])-1].extend(crates[int(data[3])-1][-(int(data[1])):])
			crates[int(data[3])-1][-(int(data[1])):] = []

top_crates = ""
for crate in crates:
	top_crates += crate[-1]

print(top_crates)