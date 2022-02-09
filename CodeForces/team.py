problems = int(input())
problems_to_solve = 0

for i in range(problems):
    sure = list(int(x) for x in input().split(" "))

    if sum(sure) >= 2:
        problems_to_solve += 1

print(problems_to_solve)
