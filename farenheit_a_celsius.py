print("Este programa transforma grados farenheit a grados celsius")

gr_usr = int(input("Cuantos grados quieres convertir: "))
gr_fin = (gr_usr - 32)/1.8

print("{} grados fahrenheit son {} grados celsius/centigrados".format(gr_usr, gr_fin))