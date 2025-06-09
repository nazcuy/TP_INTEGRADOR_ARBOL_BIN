# TRABAJO PRÁCTICO INTEGRADOR
# PROGRAMACIÓN 1
# TOMÁS ANCHORENA - AZCUY NICOLÁS

# Crea un nodo representado como una lista [nodo, hijo izquierdo, hijo derecho]
# Cada ingreso corresponde al código de un libro nuevo ingresado al catálogo.
def crear_nodo(cod_libro):
    return [cod_libro,[],[]]

# INGRESAR #
def ingresar(catalogo, cod_libro):
    # Se verifica si el catálogo está vacío. Si lo está, llama a la función crear_nodo:
    if catalogo == []:
        return crear_nodo(cod_libro)
    
    # Se obtiene el código del libro de la raíz actual del catálogo:
    raiz = catalogo[0]

    # Se compara el nuevo código con la raiz:
    if cod_libro < raiz:
        # Si es menor se inserta como hijo izquierdo:
        catalogo[1] = ingresar(catalogo[1], cod_libro)
    elif cod_libro > raiz:
        # Si es mayor se inserta como hijo derecho:
        catalogo[2] = ingresar(catalogo[2], cod_libro)
    #
    return catalogo


# ELIMINAR # 
def encontrar_min(subarbol):
    actual = subarbol
    while actual[1] != []:
        actual = actual[1]
    return actual[0]


def eliminar(catalogo, cod_libro):
    # Verifica si el catálogo está vacío. Si lo está, retorna la lista vacía.
    if catalogo == []:
        return []
    # Se obtiene el código del libro de la raíz actual del catálogo:
    raiz = catalogo[0]
    # Se compara el nuevo código con la raiz:
    if cod_libro < raiz:
        # Si es menor, se llama a la función eliminar de forma recursiva...............................
        catalogo[1] = eliminar(catalogo[1], cod_libro)
    elif cod_libro > raiz:
        # Si es mayor, se llama a la función eliminar de forma recursiva................................
        catalogo[2] = eliminar(catalogo[2], cod_libro)
    # Encontramos el nodo a eliminar
    else:
        # Si el nodo no tiene hijos (hoja), retorna la lista vacía.
        if catalogo[1] == [] and catalogo[2] == []:
            return []
        
        # Si el nodo tiene un solo hijo (nodo rama)
        elif catalogo[1] == []:
            return catalogo[2]
        elif catalogo[2] == []:
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

# MODIFICAR #
def modificar(catalogo, libro_antiguo, libro_nuevo):
    # Modifica un libro existente en el catálogo.
    # Primero eliminamos el código del libro antiguo
    catalogo = eliminar(catalogo, libro_antiguo)
    # Luego insertamos el nuevo código del libro
    return ingresar(catalogo, libro_nuevo)


# VISUALIZAR # 
def buscar_nodo(arbol, valor_buscado):
    if arbol == []:
        return None # <- Si no se encuentra ningún elemento, se retorna None para indicarlo
    # Si el valor del nodo actual es el valor buscado, significa que encontramos el nodo
    if arbol[0] == valor_buscado:
        return arbol
    # Si el valor es menor al valor del nodo actual, significa que solo puede estar en el subarbol izq.
    elif valor_buscado < arbol[0]:
        return buscar_nodo(arbol[1], valor_buscado)
    # Caso contrario, si el valor no es menor ni es igual, por descarte es el mayor
    else:
        return buscar_nodo(arbol[2], valor_buscado)
    
def calcular_peso(arbol):
    # Si el arbol está vacío, se retorna 0
    if arbol == []:
        return 0
    # Sino, el peso se calcula sumando 1 más el peso de todos los subarboles izquierdo y derecho
    return 1 + calcular_peso(arbol[1]) + calcular_peso(arbol[2])

def calcular_grado(nodo):
    # Inicializamos grado en 0
    grado = 0
    # Si la referencia al hijo izquierdo no está vacía, significa que el nodo tiene un hijo izquierdo 
    # por lo que se incrementa el grado en 1
    if nodo[1] != []:
        grado += 1
    # Si la referencia al hijo derecho no está vacía, significa que el nodo tiene un hijo derecho 
    # por lo que se incrementa el grado en 1 
    if nodo[2] != []:
        grado += 1
    return grado

def visualizar(arbol, valor_buscado):
    # Intenta encontrar el nodo con el valor buscado en el árbol
    nodo = buscar_nodo(arbol, valor_buscado)
    # Si es None, no encontró el valor
    if nodo is None:
        print("El código no se encuentra en el catálogo.")
    # Caso contrario, si el nodo fue encontrado, se muestra la información del código encontrado
    else:
        print(f"\nInformación del código {valor_buscado}:")
        print(f"Peso total del árbol: {calcular_peso(arbol)}")
        print(f"Grado del nodo: {calcular_grado(nodo)}")

    
# ORDENES DE RECORRIDO
def preorden(arbol):
    # Si el árbol no está vacío, se ejecuta lo siguiente
    if arbol != []:
        # Mostramos el valor del nodo actual
        print(arbol[0])
        # Recorremos de manera recursiva ambos subarboles
        preorden(arbol[1])
        preorden(arbol[2])
    # Si el árbol está vacío, la función termina con return
    else:
        return

def inorden(arbol):
    # Igual que en el preorden, chequeamos el valor de arbol
    if arbol != []:
        # Recorremos subarbol izquierdo
        inorden(arbol[1])
        # Mostramos el valor del nodo actual
        print(arbol[0])
        # Recorremos subarbol derecho
        inorden(arbol[2])
    # Si el árbol está vacío, la función termina con return
    else:
        return

def postorden(arbol):
    # Nuevamente, arból con elementos, ejecutamos lo de adentro
    if arbol != []:
        # Se recorre recursivamente el subarbol izquierdo
        postorden(arbol[1])
        # Se recorre recursivamente el subarbol derecho
        postorden(arbol[2])
        # Se imprime el valor del nodo actual
        print(arbol[0])
    # Si el árbol está vacío, la función termina con return
    else:
        return



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
    print("\nAPLICACIÓN GESTIÓN DE BIBLIOTECA")
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
            if catalogo == []:
                print("Catálogo vacío.")
            else:
                valor = int(input("Ingrese el código del libro a visualizar: "))
                visualizar(catalogo, valor)
        elif opcion == 5:
            if catalogo == []:
                print("Catálogo vacío.")
            else:
                print("Listado en recorrido Preorden:")
                preorden(catalogo)
        elif opcion == 6:
            if catalogo == []:
                print("Catálogo vacío.")
            else:
                print("Listado en recorrido Inorden:")
                inorden(catalogo)
        elif opcion == 7:
            if catalogo == []:
                print("Catálogo vacío.")
            else:
                print("Listado en recorrido Postorden:")
                postorden(catalogo)
        elif opcion == 8:

        else:
            print("Opción inválida. Intente nuevamente.")