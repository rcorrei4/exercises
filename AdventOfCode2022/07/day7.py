input_data = open('input.txt', 'r').read().split('\n')
filesystem = []
directory = {}
listing = False

for line in input_data:
	line = line.split()

	if listing and line[0] != '$':
		if line[0] == 'dir':
			directory[line[1]] = {}
		else:
			directory[int(line[0])] = line[1]
		filesystem.append(directory)
	else:
		directory = {}
		if line[-1] == '/':
			pass
		elif line[0] == '$' and line[1] == 'ls':
			listing = True
		elif line[0] == '$' and line[1] == 'cd':
			line[2] = {}

print(filesystem)

