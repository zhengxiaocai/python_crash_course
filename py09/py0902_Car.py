from py09.car import Car, ElectricCar, Battery

if __name__ == '__main__':
    my_new_car = Car('audi', 'a4', 2020)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()

    my_new_car.update_odometer(20)
    my_new_car.read_odometer()

    my_new_car.update_odometer(30)
    my_new_car.read_odometer()

    my_new_car.increment_odometer(20)
    my_new_car.read_odometer()

    my_tesla = ElectricCar('tesla', 'model s', 2020)
    print(my_tesla.get_descriptive_name())

    my_tesla.battery.describe_battery()

    my_tesla.fill_gas_tank()

    my_tesla.battery.get_ran()
