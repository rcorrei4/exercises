ans = []

for line in sys.stdin:
	nums = line.split()
	ans.extend([int(num) ** 0.5 for num in nums if num])
for root in ans[::-1]:
	print("%.4f" % root)