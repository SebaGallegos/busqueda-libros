from busqueda import busqueda

def main():
    bus = busqueda()

    filtro = input('Bienvenido\n¿Que es lo que desea buscar? (nombre/autor): ')

    if filtro.lower() == 'nombre' or filtro.lower() == 'autor':
        print(bus.leer_archivo())
        bus.buscar(filtro)

if __name__ == '__main__':
    main()