"""
Para este ejercicio, deberás crear una clase que representa una matriz. 
Las operaciones que esta clase debe permitir son la creación de una matriz a partir de una lista de listas, 
la impresión de la matriz en una forma legible, y 
el cálculo de la transpuesta de la matriz
"""

class Matriz():
    def __init__(self, elemetos: list):
        self.elementos = elemetos

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