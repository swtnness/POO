class Gatos:
    especie = "Felino"
    color = "Blanco y negro"
    peso = 4
    medidaPeso = "Kg"
    nombre = "Kiwi"
    
    def __init__(self, nombre, color, peso): 
        self.nombre = nombre
        self.color = color
        self.peso = peso
        self.medidaPeso = self.medidaPeso
        
    def mascota(self):
        return f"Mi mascota se llama {self.nombre} y es color {self.color} y pesa {self.peso} {self.medidaPeso}"
    
gato1 = Gatos("Kiwi", "Blanco y negro", 4)
gato2 = Gatos ("Coco", "Gris", 5)

print(gato1.mascota())
print(gato2.mascota())   
print(Gatos.especie)