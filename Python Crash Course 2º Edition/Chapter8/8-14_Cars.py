def car_info(manufactor, modelname, **info):
    car = {}
    car['manufactor'] = manufactor
    car['model'] = modelname
    for key, value in info.items():
        car[key] = value
    return car

first_car = car_info('volksvagem', 'gol',
                      color='black', year='1995')

print(first_car)