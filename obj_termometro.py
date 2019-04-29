class Termometro():
    def __init__(self, temperatura, unidad):
        self.temperatura = temperatura
        self.unidad = unidad
        
    def conversor(self):
        temperatura = int(input("Introduzca la temperatura "))
        unidad = str(input("Introduzca la escala de temperatura a la que quiere convertir C/F "))
        unidad = unidad.upper()
        
        if unidad == 'C':
            temperatura = (temperatura * 9 / 5) + 32
        elif unidad == 'F':
            temperatura = (temperatura - 32) * 5 / 9
        else:
            print("La escala introducida no corresponde a ninguna conocida")
            
        return "La temperatura correspondiente a {} es {:.2f}".format(unidad, temperatura)
    
centigrado = Termometro(0, '')
farenheit = Termometro(0, '')
