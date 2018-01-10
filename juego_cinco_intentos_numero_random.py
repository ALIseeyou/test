import random
print("En este juego, debes tratar de adivinar un numero del uno al diez, tienes 5 vidas <3 ")
guess_number = (random.randrange(11))

user_number = int(input("Introduce tu numero: "))
win = ("Ganaste felicidades!! ")
lose = ("Perdiste")
total_lose = ("Perdiste las 5 vidas, vaya noob mira que era facil, el numero era {} =)".format(guess_number))
retry = ("intentalo de nuevo")
##player_lives = 5

if guess_number == user_number:
    print (win)
else:
    print(lose, retry,"te quedan 4 vidas")

user_number = int(input("Intentalo de nuevo: "))


if guess_number == user_number:
    print (win)
else:
    print(lose, retry, "te quedan 3 vidas")

user_number = int(input("Intentalo de nuevo: "))


if guess_number == user_number:
    print (win)
else:
    print(lose, retry, "te quedan 2 vidas")

user_number = int(input("Intentalo de nuevo: "))


if guess_number == user_number:
    print (win)
else:
    print(lose, retry, "te quedan 1 vidas")

user_number = int(input("Intentalo de nuevo: "))


if guess_number == user_number:
    print (win)
else:
    print(total_lose)




