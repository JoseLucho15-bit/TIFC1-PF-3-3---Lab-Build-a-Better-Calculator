import math

def addmultiplenumbers(numbers):
    """
    Recibe una lista de números y devuelve la suma total.
    Ej: addmultiplenumbers([1,2,3]) -> 6
    """
    total = 0
    for n in numbers:
        total += n
    return total


def multiplymultiplenumbers(numbers):
    """
    Recibe una lista de números y devuelve la multiplicación acumulada.
    Ej: multiplymultiplenumbers([2,3,4]) -> 24
    """
    result = 1
    for n in numbers:
        result *= n
    return result


def isitaninteger(num):
    """
    Devuelve True si num es un entero (ej 5 o 5.0), False si no.
    """
    # Si es bool, no lo consideramos entero para el ejercicio
    if isinstance(num, bool):
        return False

    # Si es int directo
    if isinstance(num, int):
        return True

    # Si es float, verificamos si no tiene parte decimal
    if isinstance(num, float):
        return num.is_integer()

    # Si es otro tipo numérico raro, intentamos convertir
    try:
        f = float(num)
        return f.is_integer()
    except:
        return False


def isiteven(num):
    """
    Devuelve True si num es un número entero y además es par.
    """
    if not isitaninteger(num):
        return False

    # Convertimos a int seguro (ej 4.0 -> 4)
    return int(num) % 2 == 0


def main():
    print("=== Calculadora Mejorada ===")
    print("1) Sumar varios números")
    print("2) Multiplicar varios números")
    print("3) Verificar si es entero")
    print("4) Verificar si es par")
    print("5) Salir")

    while True:
        opcion = input("\nElige una opción (1-5): ").strip()

        if opcion == "1":
            datos = input("Ingresa números separados por espacio: ").split()
            nums = [float(x) for x in datos]
            print("Suma =", addmultiplenumbers(nums))

        elif opcion == "2":
            datos = input("Ingresa números separados por espacio: ").split()
            nums = [float(x) for x in datos]
            print("Multiplicación =", multiplymultiplenumbers(nums))

        elif opcion == "3":
            n = float(input("Ingresa un número: "))
            print(isitaninteger(n))

        elif opcion == "4":
            n = float(input("Ingresa un número: "))
            print(isiteven(n))

        elif opcion == "5":
            print("Chao 👋")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()
