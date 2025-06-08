## Video por la profesora Trapé ## 

# Objetivos de la Investigación:
Representación con Listas: Comprender como representar arboles binarios utilizando únicamente listas en Python
Operaciones Básicas: Implementar inserción y recorridos fundamentales sobre estructuras de árbol
Evaluación Comparativa: Analizar ventajas y desventajas frente a otros tipos de implementaciones
Herramienta Educativa: Promover el uso de representaciones simples en la enseñanza de estructura de datos

# ¿Qué es un árbol?
Es una estructura de datos jerarquica compuesta por nodos conectados. El nodo superior se denomina raíz, y
cada nodo puede tener cero o más nodos hijos.
## Arbol Binario
Es un caso particular donde cada nodo tiene como máximo dos hijos: izquierdo o derecho
Esta restricción simplifica muchas operaciones y algoritmos.

# Propiedades Clave de los Árboles Binarios
Raíz: Nodo inicial del árbol, punto de entrada para todas las operaciones
Subárboles: Cualquier nodo junto a sus descendientes forma un subárbol independiente
Hojas: Nodos terminales que no tienen hijos, representan los extremos del árbol
Altura: Número de niveles desde la raíz hasta la hoja más profunda

# Nuestro Enfoque con Listas
Vamos a representar un árbol con listas, ¿que representamos de cada nodo?
Su valor, lo que sería el subárbol izquierdo y derecho, se representa en este orden
El primer elemento de la lista va a ser el valor del nodo
El segundo elemento va a ser el subárbol izquierdo
El tercer elemento va a ser el subárbol derecho

# Metodología de Desarrollo
Python 3.x
Cada nodo como lista de tres elementos: valor, subárbol izquierdo, subárbol derecho
Creación de funciones para inserción, recorridos y visualización

## FUNCIONES ##
# Crear Árbol: 
Input: El usuario va ingresando elemento a elemento, acá decidimos nosotros cómo queremos
que se ingresen los datos, el usuario teniendo la opción de agregar subárbol izquierdo, subárbol derecho
o si nosotros le preguntamos cual quiere que vaya en el subárbol izquierdo, derecho, y así
Proceso: Se genera el árbol respetando la jerarquía
Output: Se imprime por pantalla el árbol generado por el usuario
# Visualizar árbol (re contra opcional):
Input: El usuario ingresa el árbol a visualizar; la lista como está
Proceso: Se va recorriendo nodo por nodo de forma ordenada
Output: Se imprime por pantalla una forma visual del árbol 'friendly' para el usuario
# Insertar a la izquierda / derecha
Input: Nuevamente, decidimos nosotros cómo queremos realizar este diseño. 
Si queremos una función que sea insertar a la izquierda y otra insertar a la derecha, simplisimo
O directamente una función que sea insertar y pedirle al usuario a donde quiere insertar, si izquierda
o derecha, complejisimo
Proceso: Se inserta el elemento en la posición indicada
Output: Se imprime el árbol resultante por pantalla. Acá podríamos hacer uso de la función creada
anteriormente que era imprimir el árbol por pantalla (no repetir código innecesario)
# Recorrido en preorden / postorden / inorden
Input: El usuario ingresa el árbol a recorrer y el modo a de recorrido
Proceso: Se recorre el árbol en el orden que me pidió el usuario, por ejemplo puedo pedirle que me ingrese
el árbol pero que también ingrese si lo quiere recorrer en preorden / postorden / inorden.
Output: Los nombres de los nodos en el orden estipulado, puede ser string, lista, el tipo de datos que
consideremos siempre y cuando respetemos el orden que pidió el usuario (como listar los nodos en el orden
que pidió el usuario)

# Ventajas del Enfoque con Listas
Sencillez Conceptual
Bajo Nivel de Complejidad
Ideal para Principiantes

# Desventajas del Enfoque
Menor Flexibilidad
Ausencia de Encapsulamiento ¿?
Dificultad para Árboles Complejos






