sandwich_orders = ['x-burger', 'x-all', 'x-salad', 'x-bacon']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    print('I made your', sandwich_order.title())
    finished_sandwiches.append(sandwich_order)

print('\nHere is all the sandwiches: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())