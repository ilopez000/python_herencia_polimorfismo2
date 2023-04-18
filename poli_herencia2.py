class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, bono):
        super().__init__(nombre, edad, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


class Vendedor(Empleado):
    def __init__(self, nombre, edad, salario_base, comision, ventas):
        super().__init__(nombre, edad, salario_base)
        self.comision = comision
        self.ventas = ventas

    def calcular_salario(self):
        return self.salario_base + (self.comision * self.ventas)


def imprimir_salario(empleado):
    print(f"El salario de {empleado.nombre} es: {empleado.calcular_salario()}")


if __name__ == "__main__":
    empleado1 = Empleado("Pedro", 30, 2000)
    gerente1 = Gerente("María", 40, 3000, 1000)
    vendedor1 = Vendedor("Juan", 25, 1500, 0.1, 5000)

    imprimir_salario(empleado1)
    imprimir_salario(gerente1)
    imprimir_salario(vendedor1)