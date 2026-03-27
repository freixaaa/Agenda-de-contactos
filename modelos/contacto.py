class contacto:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get("nombre", "")
        self.telefono = kwargs.get("telefono", "")
        self.email = kwargs.get("email", "")
        self.residencia = kwargs.get("residencia", "")
        self.salario = kwargs.get("salario", "")
        self.peso = kwargs.get("peso", "")
        self.edad = kwargs.get("edad", "")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "residencia": self.residencia,
            "salario": self.salario,
            "peso": self.peso,
            "edad": self.edad
        }
