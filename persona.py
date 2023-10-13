class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
        
    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

    def get_sexo(self):
        return self._sexo

    def set_sexo(self, sexo):
        self._sexo = sexo
