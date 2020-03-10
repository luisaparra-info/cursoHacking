def excepcion_basica(numero):
    """Ejemplo de control de excepciones básico.
       Cualquier error desencadendo en las líneas delimitadas será capturado sin hacer nada. """
    try:

        numero = float(numero)
        print("La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5))
    except:
        pass
    print("Ejecuto esta sentencia")

print("Batería de pruebas excepcion_basica");
excepcion_basica(-1)
excepcion_basica(13j)
excepcion_basica("Hola")
excepcion_basica("15")

def excepcion_simple(numero):
    """ Ejemplo de control de excepciones básico. Cualquier error desencadendo
        en las líneas delimitadas ejecutará el bloque de código anidado en except."""

    ocurre_error = False
    try:
        numero = float(numero)
        print("La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5))
    except:
        ocurre_error = True
    if ocurre_error:
        print("ERROR.")
    else:
        print("OK.")

print("Batería de pruebas excepcion_simple");
excepcion_simple(-1)
excepcion_simple(13j)
excepcion_simple("Hola")
excepcion_simple("15")

def excepciones_identificadas(numero):
    """ Ejemplo de control de excepciones para diversos errores identificados.
        En caso de que ocurra un error inesperado, se desplegará una advertencia.
        El programa pedirá un número y desplegará la raíz cuadrada de dicho número."""
    ocurre_error = False
    try:
        numero = float(numero)
        print("La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5))

    except TypeError:
        ocurre_error = True
        print("Ocurrió un error previsto.")
    except:
        ocurre_error = True
        print("¡No sé qué pasó!")

    if ocurre_error:
        print("ERROR.")
    else:
        print("OK")

print("Batería de pruebas excepciones_identificadas");
excepciones_identificadas(-1)
excepciones_identificadas(13j)
excepciones_identificadas("Hola")
excepciones_identificadas("15")

def excepciones_descritas(numero):
    """ Ejemplo de control de excepciones para diversos errores identificados.
        En caso de que ocurra un error inesperado, se desplegará una advertencia.
        La advertencia incluirá el mensaje de Python que describe el error.
        El programa pedirá un número y desplegará la raíz cuadrada de dicho número.
        """
    ocurre_error = False
    try:
        numero = float(numero)
        print("La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5))
    except TypeError as descripcion:
        ocurre_error = True
        print("Ocurrió un error previsto:", descripcion)
    except:
        ocurre_error = True
        print("¡No sé qué pasó!")
    if ocurre_error:
        print("ERROR.")
    else:
        print("OK.")

print("Batería de pruebas excepciones_descritas");
excepciones_descritas(-1)
excepciones_descritas(13j)
excepciones_descritas("Hola")
excepciones_descritas("15")


def excepciones_atrapadas(numero):
    """ Ejemplo de control de excepciones para diversos errores.
        Desplegará el cuadrado de dicho número.
        En caso de ocurrir una excepción se despelgará el mensaje de error."""

    ocurre_error = True
    try:
        numero = float(numero)
        print("La raíz cuadrada de %f es %f" % (numero, numero ** 0.5))
    except (ValueError, TypeError) as excepcion:
        print("Mensaje de error:", excepcion)
    except:
        print("¡No sé qué pasó!")
    else:
        print("No hubo errores.")
        ocurre_error = False
    finally:
        if ocurre_error:
            print("ERROR.")
        else:
            print("¡OK!")
    print("FIN.")


print("Batería de pruebas excepciones_atrapadas");

excepciones_atrapadas(-1)
excepciones_atrapadas(13j)
excepciones_atrapadas("Hola")
excepciones_atrapadas("15")

def levanta_excepcion(numero):
    """ Levantará una excepción con un mensaje propio en caso de que
        el número ingresado sea negativo.
        El programa pedirá un número y desplegará la raíz cuadrado de dicho número.
        En caso de que ocurra un error definido, el programa desplegará el mensaje
        correspondiente."""

    ocurre_error = True

    try:
        if numero < 0:
            raise TypeError("No es posible calcular la raíz de un negativo.")
        print("La raíz cuadrada de %.2f es %.2f" % (numero, numero ** 0.5))
    except (TypeError) as mensaje:
        print("Ocurrió una excepción identificada.", mensaje)
    except ValueError as mensaje:
        print(mensaje)
    except:
        print("¡No sé qué pasó!")
    else:
        print("No hubo errorres.")
        ocurre_error = False
    finally:
        if ocurre_error:
            print("ERROR.")
        else:
            print("¡OK!")

print("Batería de pruebas levanta_excepciones");

levanta_excepcion(-1)
levanta_excepcion("Hola")
levanta_excepcion(15)

def condiciona():
    """Genera una excepción cuando la palabra clave coincide con el
    valor indicado.
    El programa se detendrá sólo si se escribe la palabra clave."""

    itera = True
    while itera:
        try:
            clave = input("Dame la clave: ")
            assert(clave != "Alto")
        except AssertionError:
            print("Exacto.")
            break
condiciona()

def jerarquia_excepciones():
    try:
        a = 3/0

    except ZeroDivisionError:
        print('ZeroDivisionError: ')
    except ArithmeticError:
        print('ArithmeticError')
    except:
        print('No sé que pasó')

jerarquia_excepciones()
