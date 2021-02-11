
pizzas = ['portuguesa', 'calabresa', 'catupiry']
for pizza in pizzas:
        print(f'I really like {pizza.title()} pizza!')
print('\nPizza is in my entire life')

friend_pizzas = pizzas[:]
pizzas.append('mussarela')
friend_pizzas.append('quatro_queijos')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
