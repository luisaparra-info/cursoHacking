
###############################
#   OPERADORES DE ASIGNACIÓN  #
###############################
a, b, c = 21, 10, 0

print ("Valor de variable 'a':", a)
print ("Valor de variable 'b':", b)

c = a + b
print ("Operador = | El valor de variable 'c' es ", c)

c += a
print ("Operador += | El valor de variable 'c' es ", c)

c *= a
print ("Operador *= | El valor de variable 'c' es ", c)

c /= a
print ("Operador /= | El valor de variable 'c' es ", c)

c = 2
c %= a
print ("Operador %= | El valor de variable 'c' es ", c)

c **= a
print ("Operador **= | El valor de variable 'c' es ", c)

c //= a
print ("Operador //= | El valor de variable 'c' es ", c)
###############################
#      OPERADORES ARITMÉTCOS  #
###############################
"""
+ SUMA
- RESTA
* MULTIPLICACIÓN
** EXPONENTE
/ DIVISIÓN
// DIVISIÓN ENTERA
% MÓDULO

"""

a, b, c, d = 26, 11.3, 5, 3.5

# Suma, Añade valores a cada lado del operador
print(a + b)

# Resta, Resta el operando de la derecha del operador del lado izquierdo
print(c - a)

# Multiplicación, Multiplica los valores de ambos lados del operador
print(d * c)

# Exponente, Realiza el cálculo exponencial (potencia) de los operadores
print(c ** 2)

# División
print(float(c) / a)

# Cociente de una división, La división de operandos que el resultado es el cociente
# en el cual se eliminan los dígitos después del punto decimal.
print(a // c)

# Modulo, Divide el operando de la izquierda por el
# operador del lado derecho y devuelve el resto.
print(7 % 3)
###############################
#    OERADORES RELACIONALES   #
###############################
a, b, a1, b1, c1 = 5, 5, 7, 3, 3
cadena1, cadena2 = 'Hola', 'Adiós'
lista1, lista2 = [1, 'Lista Python', 23], [11, 'Lista Python', 23]

# Igual
c = a == b
print (c)

cadenas = cadena1 == cadena2
print (cadenas)

listas = lista1 == lista2
print (listas)

# Diferente
d = a1 != b
print (d)

cadena0 = cadena1 != cadena2
print (cadena0)

# Menor que
f = b1 < a1
print (f)

# Mayor que
e = a1 > b1
print (e)

# Menor o igual que
h = b1 <= c1
print (h)

# Mayor o igual que
g = b1 >= c1
print (g)

###############################
#    OERADORES LÓGICOS        #
###############################
# and
# or
# not


# and
print(1>0 and 1>1)
print(1>0 & 1>1)

# or
print(1>2 or 2>5)
print(1>2 | 2>5)
# not
print(not True)

