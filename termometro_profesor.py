class Termometro():
    def __init__(self):
        self.__unidadM = 'C'
        self.__temperatura = 0
        
    def __str__(self):
        return "{:.2f}º {}".format(self.__temperatura, self.__unidadM)
    
    # Métodos getter y setter de unidadM
    def unidadMedida(self, uniM = None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
                
    # Métodos getter y setter de temperatura
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
    
    # Método que mide la temperatura.
    def mide(self, uniM = None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == 'C' or uniM == 'F':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()
        
    # Metodo que convierte la temperatura medida a una unidad determinada
    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{:.2f}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{:.2f}º C".format((temperatura - 32) * 5/9)
        else:
            return "La escala introducida es incorrecta"
    