def car_info(manufactor, modelname, **info):
    car = {}
    car['manufactor'] = manufactor
    car['model'] = modelname
    for key, value in info.items():
        car[key] = value
    return car
