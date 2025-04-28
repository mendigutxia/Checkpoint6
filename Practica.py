# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de nombre_usuario y una contraseña.
# Crea un objeto usando la clase.

class Usuario:
    def __init__(self, usu, contras):
        self._nombre_usuario = usu
        self._contrasena = contras

    @property
    def nombre_usuario(self):
        return self._nombre_usuario
    
    @nombre_usuario.setter
    def nombre_usuario(self, valor):
        self._nombre_usuario = valor

    @property
    def contrasena(self):
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, valor):
        self._contrasena = valor

##----------------------------------------------------------------------------------------------##

usu1 = Usuario('Sisebuto', 'reygodo')

print(usu1.nombre_usuario)
usu1.nombre_usuario = 'Wanba'
print(usu1.nombre_usuario)

print(usu1.contrasena)
usu1.contrasena = 'reyvisigodo'
print(usu1.contrasena)
