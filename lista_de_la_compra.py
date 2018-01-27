lista_compra = []
ind_actual = 0

inp_usuario = input("¿Que desea añadir a su lista? (Escriba FIN para acabar):")

while inp_usuario != "FIN" or "fin":
    lista_compra.append(inp_usuario)
    inp_usuario = input("¿Que desea añadir a su lista? (Escriba FIN para acabar):")

largo_lista = len(lista_compra)

while ind_actual < largo_lista:
    print("Hay que comprar {}".format(lista_compra[ind_actual]))
    ind_actual += 1

print("Todo esto hay que comprar")
