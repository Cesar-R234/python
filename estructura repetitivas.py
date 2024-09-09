class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)
    
    def es_equilatero(self):
        return self.lado1 == self.lado2 == self.lado3
    
    def imprimir_resultados(self):
        print("El lado mayor es:", self.lado_mayor())
        if self.es_equilatero():
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")

# Ejemplo de uso:
lado1 = float(input("Ingrese el valor del primer lado: "))
lado2 = float(input("Ingrese el valor del segundo lado: "))
lado3 = float(input("Ingrese el valor del tercer lado: "))

triangulo = Triangulo(lado1, lado2, lado3)
triangulo.imprimir_resultados()





import math

class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def valor_absoluto(self):
        return abs(self.valor)
    
    def inversa(self):
        if self.valor == 0:
            raise ValueError("La inversa de 0 no está definida.")
        return 1 / self.valor
    
    def opuesto(self):
        return -self.valor
    
    def raiz_cuadrada(self):
        if self.valor < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(self.valor)
    
    def potencia(self, exponente):
        return self.valor ** exponente
    
    def conversion_base10_a_base2(self):
        if not isinstance(self.valor, int):
            raise ValueError("La conversión solo se puede realizar para enteros.")
        return bin(self.valor)[2:]
    
    def seno(self):
        return math.sin(math.radians(self.valor))
    
    def coseno(self):
        return math.cos(math.radians(self.valor))
    
    def tangente(self):
        return math.tan(math.radians(self.valor))
    
    def cotangente(self):
        if self.tangente() == 0:
            raise ValueError("La cotangente no está definida para ángulos múltiplos de 180°.")
        return 1 / self.tangente()
    
    def secante(self):
        if self.coseno() == 0:
            raise ValueError("La secante no está definida para ángulos múltiplos de 90°.")
        return 1 / self.coseno()
    
    def cosecante(self):
        if self.seno() == 0:
            raise ValueError("La cosecante no está definida para ángulos múltiplos de 180°.")
        return 1 / self.seno()

# Ejemplo de uso:
numero = Numero(45)
print("Valor absoluto:", numero.valor_absoluto())
print("Inversa:", numero.inversa())
print("Opuesto:", numero.opuesto())
print("Raíz cuadrada:", numero.raiz_cuadrada())
print("Potencia (al cuadrado):", numero.potencia(2))
print("Conversión de base 10 a base 2:", numero.conversion_base10_a_base2())
print("Seno:", numero.seno())
print("Coseno:", numero.coseno())
print("Tangente:", numero.tangente())
print("Cotangente:", numero.cotangente())
print("Secante:", numero.secante())
print("Cosecante:", numero.cosecante())
