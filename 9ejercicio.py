from datetime import date

class Persona:
    def __init__(self, nombre, dia, mes, año):
        self.nombre = nombre
        self.dia_nacimiento = dia
        self.mes_nacimiento = mes
        self.año_nacimiento = año
    
    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.año_nacimiento
        
        # Verificar si aún no ha cumplido años en el año actual
        if (hoy.month, hoy.day) < (self.mes_nacimiento, self.dia_nacimiento):
            edad -= 1
        
        return edad
    
    def imprimir_edad(self):
        print(f"{self.nombre} tiene {self.calcular_edad()} años.")

# Ejemplo de uso:
nombre = input("Ingrese su nombre: ")
dia = int(input("Ingrese el día de su nacimiento (1-31): "))
mes = int(input("Ingrese el mes de su nacimiento (1-12): "))
año = int(input("Ingrese el año de su nacimiento: "))

persona = Persona(nombre, dia, mes, año)
persona.imprimir_edad()

