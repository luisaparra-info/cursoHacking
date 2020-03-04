class Calculadora2:
    # iniciamos con el método __init__
    def __init__(self, valor1 = 0, valor2 = 0):
        self._valor1 = valor1
        self._valor2 = valor2


    def setValor1(self, valor1):
        self._valor1 = valor1

    def setValor2(self,valor2):
        self._valor2 = valor2


    def getValor1(self):
        return self._valor1

    def getValor2(self):
        return self._valor2

    # función para sumar
    def suma(self):
        suma = self.getValor1() + self.getValor2()
        print("El resultado de la suma de los valores es: ", suma)

    # función para restar
    def resta(self):
        resta = self.getValor1() - self.getValor2()
        print("El resultado de la resta de los valores es: ", resta)

    # función para calcular el producto
    def multiplicacion(self):
        pro = self.getValor1() * self.getValor2()
        print("El resultado de la multiplicación de los valores es: ", pro)

    # función para dividir
    def division(self):
        div = self.getValor1() / self.getValor2()
        print("El resultado de la división de los valores es: ", div)

    # función para imprimir
    def imprimir(self):
        print("Los valores son: ")
        print("Valor 1: ", self.getValor1())
        print("Valor 2: ", self.getValor2())


# bloque principal
calcular = Calculadora2(10, 5)
calcular._valor2
calcular.imprimir()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()
