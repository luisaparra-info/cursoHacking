import argparse


# Función de suma
def add(a, b):
    val = a + b
    return val


# Función de resta
def sub(a, b):
    val = a - b
    return val


# Función de división
def div(a, b):
    val = a / b
    return val


# Función de multiplicación
def multi(a, b):
    val = a * b
    return val


# Main function
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num1", help="Primer operando entero", type=int)
    parser.add_argument("num2", help="Segundo operando entero", type=int)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--suma", help="Realiza la suma de los dos operandos", action="store_true")
    group.add_argument("-r", "--resta", help="Realiza la resta de los dos operandos", action="store_true")
    group.add_argument("-d", "--division", help="Realiza la división de los dos operandos", action="store_true")
    group.add_argument("-m", "--multiplica", help="Realiza la multimplicación de los dos operandos", action="store_true")


    args = parser.parse_args()

    # Optional arguments
    if args.suma:
        print("El resultado de sumar {} y {} es {}".format(args.num1, args.num2, (add(args.num1, args.num2))))
    elif args.resta:
        print("El resultado de sumar {} y {} es {}".format(args.num1, args.num2, (sub(args.num1, args.num2))))
    elif args.division:
        print("El resultado de sumar {} y {} es {}".format(args.num1, args.num2, (div(args.num1, args.num2))))
    elif args.multiplica:
        print("El resultado de sumar {} y {} es {}".format(args.num1, args.num2, (multi(args.num1, args.num2))))
    else:
        print("Error: Es necesario indicar la operación a realizar")


if __name__ == '__main__':
    Main()
