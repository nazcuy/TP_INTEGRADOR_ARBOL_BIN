def crear_nodo():

def ingresar():

def modificar():

def eliminar():

def visualizar():

def preorden():

def inorden():

def postorden():




def menu_principal():
    print("\n***MENÚ PRINCIPAL***")
    print("1. Ingrese nuevo valor.") #Hay que agregar con la lógica de que si es menor, va a la izquierda del arbol.
    print("2. Modificar valor.")
    print("3. Eliminar valor.")
    print("4. Visualizar árbol.") # Habría que mostrar cuántos grados y orden tiene el árbol. Y el peso (cantidad de nodos). Ver video
    print("5. Recorrido Preorden.")
    print("6. Recorrido Inorden.")
    print("7. Recorrido Postorden.")
    print("8. Salir.")

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    print("\nAPLICACIÓN GESTIÓN DE ÁRBOL BINARIO")
    arbol = []

    while True:
        menu_principal()
        opcion = int(input("Seleccione una opción:"))

        if opcion == 1:

        elif opcion == 2:

        elif opcion == 3:

        elif opcion == 4:

        elif opcion == 5:

        elif opcion == 6:

        elif opcion == 7:

        elif opcion == 8:

        else:
            print("Opción inválida. Intente nuevamente.")