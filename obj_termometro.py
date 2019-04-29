class Termometro():
    def __init__(self, temperatura, unidad):
        self.temperatura = temperatura
        self.unidad = unidad
        
    def conversor(self):
        temperatura = int(input("Introduzca la temperatura en grados "))
        unidad = str(input("Introduzca la escala de temperatura "\
                           "a la que quiere convertir (C/F) "))
        unidad = unidad.upper()
        
        if unidad == 'C':
            temperatura = (temperatura - 32) * 5 / 9
            unidad = 'Celsius'
        elif unidad == 'F':
            temperatura = (temperatura * 9 / 5) + 32
            unidad = 'Fahrenheit'
        else:
            print("La escala introducida no corresponde a ninguna conocida")
            
        return "La temperatura correspondiente es {:.2f}º {}".format(temperatura, unidad)
    
escalaGrados = Termometro(0, '')
