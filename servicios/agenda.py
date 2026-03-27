from modelos.contacto import contacto

class agenda:
    def __init__(self):
        self.contactos = []
        self.ruta = ""
        self.tipo = ""

    def agregar(self, nombre, telefono, email, edad, residencia, salario, peso):
        nuevo = contacto(
            nombre=nombre,
            telefono=telefono,
            email=email,
            edad=edad,
            residencia=residencia,
            salario=salario,
            peso=peso
        )
        self.contactos.append(nuevo)

    def buscar_nombre(self, texto):
        return [c for c in self.contactos if texto.lower() in c.nombre.lower()]

    def buscar_telefono(self, texto):
        return [c for c in self.contactos if texto in str(c.telefono)]

    def promedio_edad(self):
        edades = [int(c.edad) for c in self.contactos if c.edad != ""]
        if not edades:
            return 0
        return sum(edades) / len(edades)

    def mostrar(self):
        return self.contactos
