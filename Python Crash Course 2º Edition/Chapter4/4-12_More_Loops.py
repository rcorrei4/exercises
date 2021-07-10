my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for friend in friend_foods:
    print(friend.title())
