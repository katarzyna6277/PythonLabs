import abc

class ComponentI:

    @abc.abstractmethod
    def count(self):
        pass

class Component(ComponentI):

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.components = []

    def count(self):
        count = self.price
        for component in self.components:
            count += component.count()
        return count


    def addComponent(self, component):
        self.components.append(component)


def main():
    plyta_montazowa = Component("płyta montażowa", 0)
    plyta_montazowa.addComponent(Component("dysk", 1200))
    plyta_montazowa.addComponent(Component("płyta główna", 2400))
    plyta_montazowa.addComponent(Component("ładowarka", 70))
    plyta_montazowa.addComponent(Component("jeszcze jeden dodatek", 20))


    plyta_glowna = Component("płyta główna", 700)
    plyta_glowna.addComponent(Component("procesor", 1220))
    plyta_glowna.addComponent(Component("pamięć ram", 250))
    plyta_glowna.addComponent(Component("pamięć rom", 200))

    plyta_montazowa.addComponent(plyta_glowna)


    print("Cena płyty_głównej wraz z komponentami" + plyta_glowna.count())
    print("Cena płyty_montażowej wraz z komponentami" + plyta_montazowa.count())


if __name__ == '__main__':
    main()