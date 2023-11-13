import car


class ElectricCar(car.Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = car.Battery()


car = ElectricCar('tesla', 'model s', 2018)

car.battery.describe_battery()
car.battery.upgrade_battery()
car.battery.describe_battery()
