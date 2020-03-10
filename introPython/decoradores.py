"""
Clase de ejemplo para el uso de @classmethod y @staticmethod
"""


class MiClase(Exception):
    """
    Clase de ejemplo
    """
    valor = 5

    def suma1(self, valor1, valor2):
        """
        Definimos un metodo que se llama unicamente desde una instancia de la
        clase, el cual recibe implicitamente una instancia al objeto como primer
        argumento
        Solo se puede llamar con una instancia a la clase
            ObjetoMiClase = MiClase()
            ObjetoMiClase.suma1(n,n)
        """
        return valor1 + valor2 + self.valor

    @staticmethod
    def suma2(valor1, valor2):
        """
        Definimos el metodo como @staticmethod, lo cual se podra ejecutar
        directamente como si fuera una funcion:
            MiClase.suma1(n,n)
        o con la instancia:
            ObjetoMiClase = MiClase()
            ObjetoMiClase.suma2(n,n)
        No tendra relación con el objeto donde se encuentra
        """
        return valor1 + valor2

    @classmethod
    def suma3(cls, valor1, valor2):
        """
        Definimos el metodo como @classmethod, lo cual se podra ejecutar
        directamente como si fuera una funcion:
            MiClase.suma1(n,n)
        o con la instancia:
            ObjetoMiClase = MiClase()
            ObjetoMiClase.suma3(n,n)
        Tendra acceso al contenido del objeto aunque no este instanciado
        """
        return valor1 + valor2 + cls.valor


# llamamos a las metodos sin instanciar la clase
print("Sin instancia")
print("-------------")
print("MiClase.suma2(1, 2)", MiClase.suma2(1, 2))  # devolvera: 3
print("MiClase.suma3(1, 2)", MiClase.suma3(1, 2))  # devolvera: 8

print("\nCon instancia")
print("---------------")
ObjetoMiClase = MiClase()
# llamamos a los metodos con una instancia de la clase
print("ObjetoMiClase.suma1(1, 2)", ObjetoMiClase.suma1(1, 2))  # devolvera: 8
print("ObjetoMiClase.suma2(1, 2)", ObjetoMiClase.suma2(1, 2))  # devolvera: 3
print("ObjetoMiClase.suma3(1, 2)", ObjetoMiClase.suma3(1, 2))  # devolvera: 8