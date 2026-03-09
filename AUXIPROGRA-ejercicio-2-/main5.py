from minecraft import Servidor

def main():

    servidor = Servidor()

    servidor.agregar_jugador("Steve", 120)
    servidor.agregar_jugador("Alex", 65)
    servidor.agregar_jugador("Herobrine", 300)

    servidor.verificar_stacks()
    servidor.jugador_mas_diamantes()
    servidor.total_diamantes()


if __name__ == "__main__":
    main()