def sandwiches_order(*sandwiches):
    print('\nThis is your sandwich order: ')
    for sandwich in sandwiches:
        print('-', sandwich)

sandwiches_order('salad', 'tomato', 'cheese', 'bacon')
sandwiches_order('barbecue', 'tomato', 'salad', 'hamburger')
sandwiches_order('bread', 'salad', 'tomato', 'bacon', 'hamburger', 'cheese')