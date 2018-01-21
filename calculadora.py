operacion = input("Que operación desea hacer (suma/resta/multiplicación/division/elevar)?")
primer_num = int(input("Primer numero:"))
seg_num = int(input("Segundo numero:"))
numero_final = 0
suma = primer_num + seg_num
resta = primer_num - seg_num
multiplicacion = primer_num * seg_num
division = primer_num / seg_num

if operacion == "suma":
   suma
   print("El resultado es: {}".format(suma))
elif operacion == "resta":
    resta
    print("El resultado es: {}".format(resta))
elif operacion == "multiplicacion":
    multiplicacion
    print("El resultado es: {}".format(multiplicacion))
elif operacion == "division":
    division
    print("El resultado es: {}".format(division))
