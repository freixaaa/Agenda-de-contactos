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
