numero = int(input('Introduce un numero ---> '))

print ("Que operacion desea hacer?")
print ("Suma (a)")
print ("Resta (b)")
print ("Multiplicacion (c)")
print ("Division (d)")

opcion = input('Elija una opcion ----> ')

numero2 = int(input('Introduce otro numero ----> '))

if opcion == "a":
    sum = numero + numero2
    resultado = print ('El resultado es ', sum)

elif opcion == "b":
    substraction = numero - numero2
    resultado = print ('El resultado es ', substraction)

elif opcion == "c":
    multiplication = numero * numero2
    resultado = print ('El resultado es ', multiplication)

elif opcion == "d":
    substraction = numero / numero2
    resultado = print ('El resultado es ', substraction)

cont = input("Quieres continuar? (y/n): ")

if cont == "y":

    print("Que operacion desea hacer?")
    print("Suma (a)")
    print("Resta (b)")
    print("Multiplicacion (c)")
    print("Division (d)")
    opcion = input('Elija una opcion ----> ')

    numero3 = int(input("Introduce otro numero ---->"))


    if opcion == "a":
        sum = resultado + numero3
        print('El resultado es ', sum)

    if opcion == "b":
        substraction = resultado - numero3
        print('El resultado es ', substraction)

    if opcion == "c":
        multiplication = resultado * numero3
        print('El resultado es', multiplication)

    if opcion == "d":
        substraction = resultado / numero3
        print('El resultado es ', substraction)

