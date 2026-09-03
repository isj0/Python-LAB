def build_car(make, model, **car_info):
    """Build a dictionary with arbitrary number of keyword argument."""
    car_info['manufacturer'] = make
    car_info['model_name'] = model

    return car_info

car = build_car('subaru', 'outback',
                color='blue',
                tow_package=True,
                condition='New')
print(car)