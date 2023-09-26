"""
Para este ejercicio, deberás crear una clase que representa una matriz. 
Las operaciones que esta clase debe permitir son la creación de una matriz a partir de una lista de listas, 
la impresión de la matriz en una forma legible, y 
el cálculo de la transpuesta de la matriz
"""

class Matriz():
    def __init__(self, elemetos: list):
        self.elementos = elemetos
    
    def imprimir(self):
        pass

class Transpuesta(Matriz):
    def  __init__(self, elementos):
        super().__init__(elementos)
    
    def trasnponer(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    
class Imprimir(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
    
    def imprimir(self):
        for fila in self.elementos:
            print(fila)

class Lanzador(Imprimir, Transpuesta):

    def __init__(self, elementos):
        self.elementos = elementos
        self.cantidad_filas = int(input("Ingrese la cantidad de filas: "))
        self.cantidad_columnas = int(input("Ingrese la cantidad de columnas: "))
        self.crear_matriz()
        self.matriz = Matriz(self.elementos)
        self.trasnponer = Transpuesta(self.elementos)
        self.imprimir = Imprimir(self.elementos)

    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Ingrese el elemento {i+1},{j+1}: ")))
            self.elementos.append(fila)
    
    def lanzar(self):
        print("La matriz es: ")
        self.imprimir.imprimir()
        print("La matriz transpuesta es: ")
        transpuesta = self.trasnponer.trasnponer()
        imprimir_traspuesta = Imprimir(transpuesta.elementos)
        imprimir_traspuesta.imprimir()
            
class Main():
    def __init__(self):
        self.lanzador = Lanzador([])
        self.lanzador.lanzar() 

if __name__ == "__main__":
    Main()
