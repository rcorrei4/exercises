sandwich_orders = ['x-burger', 'pastrami', 'pastrami', 'x-all', 'x-salad', 'pastrami', 'x-bacon']
finished_sandwiches = []

print('\nDeli has run out of Pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    print('I made your', sandwich_order.title())
    finished_sandwiches.append(sandwich_order)

print('\nHere is all the sandwiches: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())