class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return f'{self.nombre} dice: Guau!'


class Gato(Animal):
    def hablar(self):
        return f'{self.nombre} dice: Miau!'


class Pato(Animal):
    def hablar(self):
        return f'{self.nombre} dice: Cuac!'


def hacer_hablar(animal):
    print(animal.hablar())


def main():
    perro = Perro("Max")
    gato = Gato("Luna")
    pato = Pato("Donald")

    hacer_hablar(perro)
    hacer_hablar(gato)
    hacer_hablar(pato)


if __name__ == "__main__":
    main()
