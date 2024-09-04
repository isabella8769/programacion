from datetime import datetime #proporciona clases para maipular fechas y horas

class Calzado:
    def __init__(self, fecha_creacion, marca, tipo, numero, suela):
        # Asegurarse de que la fecha de creación es un objeto datetime
        if isinstance(fecha_creacion, str):
            try:
                self.fecha_creacion = datetime.strptime(fecha_creacion, '%Y-%m-%d')
            except ValueError:
                raise ValueError("La fecha debe estar en el formato 'YYYY-MM-DD'")
        elif isinstance(fecha_creacion, datetime):
            self.fecha_creacion = fecha_creacion
        else:
            raise TypeError("La fecha de creación debe ser una cadena o un objeto datetime")
        
        self.marca = marca
        self.tipo = tipo
        self.numero = numero
        self.suela = suela

    def __str__(self):#Proporciona una representación en cadena de la instancia de la zapatilla, incluyendo los nuevos atributos.
        return (f"Calzado(marca={self.marca}, tipo={self.tipo}, numero={self.numero}, "
                f"suela={self.suela}, fecha_creacion={self.fecha_creacion.strftime('%Y-%m-%d')})")

    def get_edad(self):
        """Calcula la edad del calzado en años."""
        today = datetime.today()
        edad = today.year - self.fecha_creacion.year - ((today.month, today.day) < (self.fecha_creacion.month, self.fecha_creacion.day))
        return edad

class Zapatilla(Calzado):
    def __init__(self, fecha_creacion, marca, tipo, numero, suela, modelo, materiales, stock):
        super().__init__(fecha_creacion, marca, tipo, numero, suela)
        self.modelo = modelo
        self.materiales = materiales
        self.stock = stock

    def __str__(self):
        return (f"Zapatilla(marca={self.marca}, tipo={self.tipo}, numero={self.numero}, "
                f"suela={self.suela}, fecha_creacion={self.fecha_creacion.strftime('%Y-%m-%d')}, "
                f"modelo={self.modelo}, materiales={self.materiales}, stock={self.stock})")

    def actualizar_stock(self, cantidad):
        """Actualiza el stock de las zapatillas."""
        if cantidad < 0 and abs(cantidad) > self.stock:
            raise ValueError("No hay suficiente stock para reducir la cantidad.")
        self.stock += cantidad

# Ejemplo de uso
zapatilla = Zapatilla('2023-05-15', 'Nike', 'Deportivo', 42, 'EVA', 'Air Max 270', 'Cuero', 100)
print(zapatilla)
print(f"Edad de la zapatilla: {zapatilla.get_edad()} años")

# Actualizar stock
zapatilla.actualizar_stock(-10)
print(f"Stock actualizado: {zapatilla.stock}")
