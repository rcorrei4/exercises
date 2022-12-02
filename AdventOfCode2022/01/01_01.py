elf_most_calories = []
with open('input.txt', 'r') as input:
	elf_calories = []
	for calorie in input.readlines():
		calorie = calorie.rstrip('\n')
		if calorie:
			elf_calories.append(int(calorie))
		else:
			if sum(elf_calories) > sum(elf_most_calories):
				elf_most_calories = elf_calories
				elf_calories = []
			else:
				elf_calories = []
				
print(sum(elf_most_calories))