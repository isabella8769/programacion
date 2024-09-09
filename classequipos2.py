class EquipoDeportivo:
    def __init__(self, nombre, fecha_creacion, precio_costo, precio_venta, descripcion, cantidad_stock):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.descripcion = descripcion
        self.cantidad_stock = cantidad_stock

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad_stock:
            self.cantidad_stock -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} unidades de {self.nombre}.")
            print(f"Cantidad original: {self.cantidad_stock + cantidad_vendida}")
            print(f"Cantidad actual: {self.cantidad_stock}")
        else:
            print("No hay suficiente stock para esta venta.")

    def __str__(self):
        return f"Nombre: {self.nombre}\nFecha de creación: {self.fecha_creacion}\nPrecio de costo: {self.precio_costo}\nPrecio de venta: {self.precio_venta}\nDescripción: {self.descripcion}\nCantidad en stock: {self.cantidad_stock}"

# Ejemplo de uso
balon_futbol = EquipoDeportivo("Balón de fútbol", "2023-11-20", 10, 15, "Balón de fútbol talla 5", 50)
raqueta_tenis = EquipoDeportivo("Raqueta de tenis", "2023-12-01", 30, 50, "Raqueta de tenis Head", 20)



balon_futbol.vender(10)
print(balon_futbol)

raqueta_tenis.vender(12)
print(raqueta_tenis)