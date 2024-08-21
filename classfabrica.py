class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    
    def mostrar_atributos(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            descuento = self.precio * 0.10
            self.precio -= descuento
            print(f"Descuento aplicado. Nuevo precio: {self.precio}")
        else:
            print("No se aplica descuento.")

class Moto(Fabrica):
    def __init__(self, color, precio):
        # Asumimos que una moto tiene 2 llantas
        super().__init__(llantas=2, color=color, precio=precio)

class Auto(Fabrica):
    def __init__(self, color, precio):
        # Asumimos que un carro tiene 4 llantas
        super().__init__(llantas=4, color=color, precio=precio)

# Crear objetos para cada clase
moto = Moto(color="Rojo", precio=120000)
auto = Auto(color="Azul", precio=95000)

# Mostrar atributos y aplicar descuento
print("Atributos de la Moto:")
moto.mostrar_atributos()
moto.aplicar_descuento()

print("\nAtributos del auto:")
auto.mostrar_atributos()
auto.aplicar_descuento()
