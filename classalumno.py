class Alumno:
    def __init__(self, nombre, nota):
        # Inicializa los atributos de la clase
        self.nombre = nombre
        self.nota = nota

    def imprimir_atributos(self):
        # Imprime el nombre y la nota del alumno
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_resultado(self):
        # Muestra el resultado basado en la nota
        if self.nota >= 7:
            resultado = "Aprobado"
        else:
            resultado = "Reprobado"
        print(f"{self.nombre} ha obtenido una nota de {self.nota} y está {resultado}.")

# Ejemplo de uso
def main():
    # Crear un objeto Alumno
    alumno1 = Alumno("Roberto Almeida", 5)
    
    # Imprimir los atributos del alumno
    alumno1.imprimir_atributos()
    
    # Mostrar el resultado del alumno
    alumno1.mostrar_resultado()

if __name__ == "__main__":
    main()
