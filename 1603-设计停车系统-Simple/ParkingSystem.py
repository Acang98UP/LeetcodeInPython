class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        return False


if __name__ == '__main__':
    car = ParkingSystem(1, 1, 0)
    print(car.addCar(1))
    print(car.addCar(2))
    print(car.addCar(3))
    print(car.addCar(1))

