print("El jugador 1 elige el numero a adivinar, y el jugador 2 trata de adivinarlo")
num_eleg = int(input("Elige tu numero: "))
num_adv = int(input("Adivina el numero: "))

while num_adv != num_eleg:
    num_adv = int(input("Intentalo otra vez: "))

print("¡¡¡Ganastee!!!")