input_data = open('input.txt', 'r').read().split('\n')

game = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

game_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

points = 0

for game_round in input_data:
    game_round = game_round.split(' ')
    game_round[1] = game[game_round[1]]

    if game_round[0] == game_round[1]:
        points +=  3
    if game_round[0] == 'A' and game_round[1] == 'B':
        points += 6
    if game_round[0] == 'B' and game_round[1] == 'C':
        points += 6
    if game_round[0] == 'C' and game_round[1] == 'A':
        points += 6
    else:
        points += 0

    points += game_points[game_round[1]]

print(points)