from csv import DictReader

class busqueda:

    def __init__(self):
        self.lista_libros = []
        self.resultados = []

    def leer_archivo(self):
        if len(self.lista_libros) != 0:
            self.lista_libros.clear()

        with open("lista_libros.csv", "r", encoding="utf8", newline = "") as archivo:
            leer_archivo = DictReader(archivo)
            for fila in leer_archivo:
                self.lista_libros.append(fila)
        
        return 'Archivo leido correctamente'

    def buscar(self, filtro):
        if len(self.resultados) != 0:
            self.resultados.clear()

        nombre = input(f"ingrese el {filtro} del libro: ")
        for fila in self.lista_libros:
            if fila[str(filtro)].lower() == nombre.lower():
                self.resultados.append(fila)

        if len(self.resultados) != 0:
            print("-"*50)
            for i in range(len(self.resultados)):
                for k,v in self.resultados[i].items():
                    print(f"{k.capitalize()}: {v}")
                print("-"*50)

