from videojuego import Videojuego
juego1 = Videojuego("FIFA", "PlayStation", 2)
juego2 = Videojuego("Minecraft", "PC", 1)

juego1.agregarJugadores()      
juego2.agregarJugadores(3)     

print("=== VIDEOJUEGOS ===")
juego1.mostrar()
juego2.mostrar()