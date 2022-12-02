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

    if game_round[1] == 'Y':
        points += game_points[game_round[0]] + 3
    elif game_round[1] == 'X':
        if game_round[0] == 'A':
            points += game_points['C']
        if game_round[0] == 'B':
            points += game_points['A']
        if game_round[0] == 'C':
            points += game_points['B']
    elif game_round[1] == 'Z':
        if game_round[0] == 'A':
            points += game_points['B'] + 6
        if game_round[0] == 'B':
            points += game_points['C'] + 6
        if game_round[0] == 'C':
            points += game_points['A'] + 6

print(points)