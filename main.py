import csv

def busquedaLibros(op):
    diccionario = []
    lista = []

    with open("lista_libros.csv", "r", newline = "") as archivo:
        leer_archivo = csv.DictReader(archivo)
        for fila in leer_archivo:
            diccionario.append(fila)

    if op.lower() == 'libro':
        nombre = input("ingrese el nombre del libro: ")
        for fila in diccionario:
            if fila['nombre'].lower() == nombre.lower():
                lista.append(fila)

        if len(lista) != 0:
            print("-"*50)
            for i in range(len(lista)):
                for k,v in lista[i].items():
                    print(f"{k}: {v}")
                print("-"*50)

    elif op.lower() == 'autor':
        autor = input("ingrese el nombre del autor: ")
        for fila in diccionario:
            if fila['autor'].lower() == autor.lower():
                lista.append(fila)
          
        if len(lista) != 0:
            print("-"*50)
            for i in range(len(lista)):
                for k,v in lista[i].items():
                    print(f"{k}: {v}")
                print("-"*50)

busquedaLibros('autor')