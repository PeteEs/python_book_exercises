def cars_fun(manufacturer,model_name,**car_info):
    
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name

    return car_info

car = cars_fun('subaru', 'outback', color='blue', tow_package=True)

print(car)