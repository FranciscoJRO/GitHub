print("***********************Hola Bienvenido a la Super-Mini Calculadora************************")
print("A continuacion se muestran las opciones de la calcludora")
print("1) Suma")
print("2) Resta")
print("3) Multiplicacion")
print("4) Division")

opcion = input("Ingrese la opcion que desea realizar: ")
if opcion == "1":
    print("Ha seleccionado la opcion suma")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    suma = n1 + n2
    print("El resultado de la suma es: ", suma)
if opcion == "2":
    print("Ha seleccionado la opcion resta")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    resta = n1 - n2
    print("El resultado de la resta es: ", resta)
if opcion == "3":
    print("Ha seleccionado la opcion multiplicacion")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    multiplicacion = n1 * n2
    print("El resultado de la multiplicacion es: ", multiplicacion)
if opcion == "4":
    print("Ha seleccionado la opcion division")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    if n2 == 0:
        print("No se puede dividir entre 0")
    division = n1 / n2
    print("El resultado de la division es: ", division)