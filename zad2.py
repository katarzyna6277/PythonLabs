import abc


class Clean:

    @abc.abstractmethod
    def wash(self):
        pass


class BubbleBath(Clean):

    def wash(self):
        print("BubbleBath")


class Watering(Clean):

    def wash(self):
        print("Watering")


class Waxing(Clean):

    def wash(self):
        print("Waxing")


class CleanWater(Clean):

    def wash(self):
        print("CleanWater")


class CarWash(Clean):

    def wash(self, whichWash):
        whichWash.wash()


def main():
    car_wash = CarWash()
    message = "1-mycie pianą\n2-spłukiwanie\n" \
              "3-woskowanie\n4-namaczanie\n5-zakończenie mycia\n"
    while True:
        option = input(message)
        if option == "1":
            car_wash.wash(BubbleBath())
        elif option == "2":
            car_wash.wash(Watering())
        elif option == "3":
            car_wash.wash(Waxing())
        elif option == "4":
            car_wash.wash(CleanWater())
        elif option == "5":
            break
        else:
            print("Brak opcji")


if __name__ == '__main__':
    main()
