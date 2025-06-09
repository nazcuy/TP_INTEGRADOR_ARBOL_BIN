# TRABAJO PRÁCTICO INTEGRADOR
# PROGRAMACIÓN 1
# TOMÁS ANCHORENA - AZCUY NICOLÁS

# Crea un nodo representado como una lista [cod_libro, hijo_izquierdo, hijo_derecho]
def crear_nodo(cod_libro):
    return [cod_libro,[],[]]

def ingresar(catalogo, cod_libro):
    # Se verifica si el árbol/subárbol está vacío. de ser verdadero llama a la función crear_nodo:
    if catalogo == []:
        return crear_nodo(cod_libro)
    
    # Se obtiene el cod_libro de la raíz actual
    raiz = catalogo[0]

    # Se compara el nuevo cod_libro con la raiz:
    if cod_libro < raiz:
        # Si es menor se inserta como hijo izquierdo:
        catalogo[1] = ingresar(catalogo[1], cod_libro)
    elif cod_libro > raiz:
        #
        catalogo[2] = ingresar(catalogo[2], cod_libro)
    #
    return catalogo


def eliminar(catalogo, cod_libro):
    # Verifica si el árbol está vacío, si está vacío, retorna la lista vacía.
    if catalogo == []:
        return []
    # Se obtiene el cod_libro de la raíz actual
    raiz = catalogo[0]
    # Busca el cod_libro en la raíz
    if cod_libro < raiz:
        catalogo[1] = eliminar(catalogo[1], cod_libro)
    elif cod_libro > raiz:
        catalogo[2] = eliminar(catalogo[2], cod_libro)
    # Encontramos el nodo a eliminar
    else:
        # Si el nodo no tiene hijos (hoja), retorna la lista vacía.
        if catalogo[1] == [] and catalogo[2] == []:
            return []
        
        # Si el nodo tiene un solo hijo (nodo rama)
        elif catalogo[1] == False:
            return catalogo[2]
        elif catalogo[2] == False:
            return catalogo[1]
        
        # Si el nodo tiene dos hijos
        else:
            # Encontrar el sucesor inorden (mínimo en subárbol derecho)
            min_val = encontrar_min(catalogo[2])
            # Reemplazar cod_libro actual por el mínimo
            catalogo[0] = min_val
            # Eliminar el cod_libro mínimo del subárbol derecho
            catalogo[2] = eliminar(catalogo[2], min_val)
    # Devolver el árbol modificado
    return catalogo


def modificar(catalogo, libro_antiguo, libro_nuevo):
    # Modifica un cod_libro existente en el árbol.
    # Primero eliminamos el cod_libro antiguo
    catalogo = eliminar(catalogo, libro_antiguo)
    # Luego insertamos el nuevo cod_libro
    return ingresar(catalogo, libro_nuevo)


def visualizar():


def orden():


def preorden():

def inorden():

def postorden():




def menu_principal():
    print("\n***MENÚ PRINCIPAL***")
    print("1. Registrar nuevo código único del libro.")
    print("2. Eliminar libro.")
    print("3. Modificar libro ingresado.")
    print("4. Visualizar datos del catálogo.")
    print("5. Listar códigos (Preorden).")
    print("6. Listar códigos (Inorden).")
    print("7. Listar códigos (Postorden).")
    print("8. Salir.")

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    print("\nAPLICACIÓN GESTIÓN DE ÁRBOL BINARIO")
    catalogo = []

    while True:
        menu_principal()
        opcion = int(input("Seleccione una opción:"))

        if opcion == 1:
            cod_libro = int(input("Ingrese un cod_libro: "))
            catalogo = ingresar(catalogo, cod_libro)
            print(f"El cod_libro {cod_libro} se ha ingresado correctamente.")

        elif opcion == 2:
            if catalogo == []:
                print("Árbol vacío.")
            else:
                cod_libro = int(input("cod_libro a eliminar: "))
                catalogo = eliminar(catalogo, cod_libro)
                print(f"cod_libro {cod_libro} eliminado correctamente.")

        elif opcion == 3:
            if catalogo == []:
                print("Árbol vacío.")
            else:
                antiguo = int(input("cod_libro a modificar: "))
                nuevo = int(input("Ingrese el nuevo cod_libro: "))
                catalogo = modificar(catalogo, antiguo, nuevo)
                print(f"El cod_libro {antiguo} fue modificado por {nuevo} correctamente.")

        elif opcion == 4:

        elif opcion == 5:

        elif opcion == 6:

        elif opcion == 7:

        elif opcion == 8:

        else:
            print("Opción inválida. Intente nuevamente.")