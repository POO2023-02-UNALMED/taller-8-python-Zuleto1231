from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
        
    def get_golesMarcados(self):
        return self._golesMarcados

    def set_golesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def get_tarjetasRojas(self):
        return self._tarjetasRojas

    def set_tarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def get_piernaHabil(self):
        return self._piernaHabil

    def set_piernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
        
    @classmethod
    def get_listaFutbolistas(cls):
        return cls.listaFutbolistas

    @classmethod
    def set_listaFutbolistas(cls, lista):
        cls.listaFutbolistas = lista
        
    def __str__(self):
        return "Mi nombre es "+ self._nombre+ " soy profesional en el deporte "+self._deporte+ " Tengo "+ str(self._edad)+ " años de edad y llevo "+ str(self._añosPracticando)+" años en el deporte"    
        

futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
print(futbolista)