from bus import Bus
def main():
    bus1 = Bus(40)

    bus1.subir_pasajeros(20)
    bus1.cobrar_pasaje()
    bus1.asientos_disponibles()
if __name__ == "__main__":
    main()