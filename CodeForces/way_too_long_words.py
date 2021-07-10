lines = int(input())
words = []

for i in range(lines):
    word = input()
    if len(word) > 10:
        words.append(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        words.append(word)

for i in words:
    print(i)
