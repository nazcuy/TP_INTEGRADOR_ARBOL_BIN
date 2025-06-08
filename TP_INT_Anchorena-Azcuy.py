# TRABAJO PRÁCTICO INTEGRADOR
# PROGRAMACIÓN 1
# TOMÁS ANCHORENA - AZCUY NICOLÁS

# Crea un nodo representado como una lista [valor, hijo_izquierdo, hijo_derecho]
def crear_nodo(valor):
    return [valor,[],[]]

def ingresar(arbol, valor):
    # Se verifica si el árbol/subárbol está vacío. de ser verdadero llama a la función crear_nodo:
    if arbol == []:
        return crear_nodo(valor)
    
    # Se obtiene el valor de la raíz actual
    raiz = arbol[0]

    # Se compara el nuevo valor con la raiz:
    if valor < raiz:
        # Si es menor se inserta como hijo izquierdo:
        arbol[1] = ingresar(arbol[1], valor)
    elif valor > raiz:
        #
        arbol[2] = ingresar(arbol[2], valor)
    #
    return arbol


def eliminar(arbol, valor):
    # Verifica si el árbol está vacío, si está vacío, retorna la lista vacía.
    if arbol == []:
        return []
    # Se obtiene el valor de la raíz actual
    raiz = arbol[0]
    # Busca el valor en la raíz
    if valor < raiz:
        arbol[1] = eliminar(arbol[1], valor)
    elif valor > raiz:
        arbol[2] = eliminar(arbol[2], valor)
    # Encontramos el nodo a eliminar
    else:
        # Si el nodo no tiene hijos (hoja), retorna la lista vacía.
        if arbol[1] == [] and arbol[2] == []:
            return []
        
        # Si el nodo tiene un solo hijo (nodo rama)
        elif arbol[1] == False:
            return arbol[2]
        elif arbol[2] == False:
            return arbol[1]
        
        # Si el nodo tiene dos hijos
        else:
            # 4.1 Encontrar el sucesor inorden (mínimo en subárbol derecho)
            min_val = encontrar_min(arbol[2])
            # 4.2 Reemplazar valor actual por el mínimo
            arbol[0] = min_val
            # 4.3 Eliminar el valor mínimo del subárbol derecho
            arbol[2] = eliminar(arbol[2], min_val)
    
    # 5. Devolver el árbol modificado
    return arbol

def modificar(arbol, valor_antiguo, valor_nuevo):
    # Modifica un valor existente en el árbol.
    # Primero eliminamos el valor antiguo
    arbol = eliminar(arbol, valor_antiguo)
    # Luego insertamos el nuevo valor
    return ingresar(arbol, valor_nuevo)

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