
ask_libros = input("¿Que clase de libros quieres que te recomiende?: ")
libros_fant = ("The King Killer Chronicles, Saga Geralt de Rivia, El señor de los anillos, Canción de Hielo y Fuego (Juego de Tronos), El Silmarillion, Memorias de Idhún, Los libros de Terramar...  ")
libros_infantiles = ("Geronimo Stilton, Diario de Greg, La historia interminable, Pinocho, Alicia en el Pais de las Maravillas ")
libros_dist = ("1984, Fahrenheit 451, La larga marcha, Traición, La Selección, Amanecer Rojo, La quinta ola, Los Juegos del Hambre, Divergent, El corredor del laberinto... ")
libros_inst = ("Nata y Chocolate, Marina, Relatos de lo inesperado, Dani Campeon del Mundo... ")
libros_bull = ("El club de los Perdedores, Cuando me veas (+/-), y luego ganas tu... ")
libros_rom = ("Eleanor y Park, El sin sentido del amor... ") ## no suelo leer de estos xddd
libros_terr = ("Dracula, It, El resplandor, Carrie, Misery, El Exorcista, Cujo, Doctor Sueño, La milla verde ")


if ask_libros == "fantasia":
    print (libros_fant)
    print(ask_libros)

if ask_libros == "infantiles":
    print (libros_infantiles)
    print(ask_libros)

if ask_libros == "distopias":
    print (libros_dist)
    print (ask_libros)
