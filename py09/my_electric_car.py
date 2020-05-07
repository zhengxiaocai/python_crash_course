from py09.car import ElectricCar

if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'tesla s', 2020)
    my_tesla.fill_gas_tank()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_ran()
