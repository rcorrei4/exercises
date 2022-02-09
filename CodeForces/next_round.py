participants_and_place = list(int(x) for x in input().split(" "))
scores = list(int(x) for x in input().split(" "))
advance_participants = 0

for i in range(participants_and_place[0]):
    if scores[i] >= scores[participants_and_place[1]-1] and scores[i] > 0:
        advance_participants += 1

print(advance_participants)
