"""Calcular el numero faltante de un conjunto de los primeros 100 números naturales
del cual se extrajo uno.
"""
import sys

class conjunto_100:
    def __init__(self):
        self.conjunto = set(range(1,101))
        self.suma = sum(self.conjunto)
    
    def extract (self, num):
        if isinstance(num, int):
            if 1 <= num <= 100:
                self.conjunto.remove(num)        
    
    def faltante (self):
        return self.suma - sum(self.conjunto)

#Pedir numero en consola y creacion de objeto conjunto
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num_a_extraer = int(sys.argv[1])
            conjunto = conjunto_100()
            conjunto.extract(num_a_extraer)
            numero_extraido = conjunto.faltante()
            print(f"En el conjunto de 1 - 100 el numero que solicito sacar es: {numero_extraido}") if numero_extraido>0 else print("Valor no existente")
        except ValueError:
            print("Error: El dato debe ser un número entero.")
    else:
        print("No se ingreso un dato para extraer")
