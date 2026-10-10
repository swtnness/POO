class Persona:
    altura = "Baja"
    raza = "Latina"
    peso = 53
    medidaPeso = "kg"
    edad = 22
    nombre = "Vannesa"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"¡Hola! Soy {self.nombre}, mi edad es {self.edad} años."


# Creación del objeto (instanciar)
persona = Persona("Vannesa", 22)

print(persona.nombre)
print(persona.presentarse())
