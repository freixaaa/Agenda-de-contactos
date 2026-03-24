from modelos.contacto import contacto

class agenda:
    def __init__(self):
        self.contactos = []
        self.ruta = ""
        self.tipo = ""

    def agregar(self, nombre, telefono, email, edad, residencia):
        nuevo = contacto(nombre, telefono, email, edad, residencia)
        self.contactos.append(nuevo)

    def buscar_nombre(self, texto):
        return [c for c in self.contactos if texto.lower() in c.nombre.lower()]

    def buscar_telefono(self, texto):
        return [c for c in self.contactos if texto in c.telefono]

    def promedio_edad(self):
        if not self.contactos:
            return 0
        return sum(c.edad for c in self.contactos) / len(self.contactos)

    def mostrar(self):
        return self.contactos
