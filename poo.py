from csv import DictReader

class busqueda:

    def __init__(self, filtro = 'nombre'):
        self.filtro = filtro
        self.lista_libros = []
        self.resultados = []

    def leer_archivo(self):
        with open("lista_libros.csv", "r", newline = "") as archivo:
            leer_archivo = DictReader(archivo)
            for fila in leer_archivo:
                self.lista_libros.append(fila)
        
        return 'Archivo leido correctamente'

    def buscar(self):
        nombre = input("ingrese el nombre del libro: ")
        for fila in self.lista_libros:
            if fila[str(self.filtro)].lower() == nombre.lower():
                self.resultados.append(fila)

        if len(self.resultados) != 0:
            print("-"*50)
            for i in range(len(self.resultados)):
                for k,v in self.resultados[i].items():
                    print(f"{k}: {v}")
                print("-"*50)

bus = busqueda()
print(bus.leer_archivo())
bus.buscar()

