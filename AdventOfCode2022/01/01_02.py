top1_most_calories = 0
top2_most_calories = 0
top3_most_calories = 0

with open('input.txt', 'r') as input:
	elf_calories = []
	input_lines = input.readlines()
	for calorie in input_lines:
		calorie = calorie.rstrip('\n')

		if calorie:
			elf_calories.append(int(calorie))
		if (not calorie or calorie == input_lines[-1].rstrip('\n')) and sum(elf_calories) not in [top1_most_calories, top2_most_calories, top3_most_calories]:
			sum_elf_calories = sum(elf_calories)
			if sum_elf_calories > top1_most_calories:
				top3_most_calories = top2_most_calories
				top2_most_calories = top1_most_calories
				top1_most_calories = sum_elf_calories
			elif sum_elf_calories > top2_most_calories:
				top3_most_calories = top2_most_calories
				top2_most_calories = sum_elf_calories
			elif sum_elf_calories > top3_most_calories:
				top3_most_calories = sum_elf_calories
			elf_calories = []
			sum_elf_calories = 0

print(top1_most_calories + top2_most_calories + top3_most_calories)