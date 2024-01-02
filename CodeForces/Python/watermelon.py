weight = int(input())

if (weight/2) % 2 == 0 or (weight-2) % 2 == 0 and weight != 2:
    print("YES")
else:
    print("NO")
