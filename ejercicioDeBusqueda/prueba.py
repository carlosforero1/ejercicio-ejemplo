from ejercicioDeBusqueda.Nodo import Nodo
from ejercicioDeBusqueda.arbolBinario import ArbolBinario


class Prueba:
    def __init__(self):
        raiz = Nodo(1)
        raiz.izquierda = Nodo(2)
        raiz.derecha = Nodo(3)
        raiz.izquierda.izquierda = Nodo(4)
        raiz.izquierda.derecha = Nodo(5)

        arbol = ArbolBinario(raiz)

        print("Recorrido preorden:")
        arbol.preorden(raiz)

        print("Recorrido en orden:")
        arbol.en_orden(raiz)

        print("Recorrido postorden:")
        arbol.postorden(raiz)

# Ejemplo de uso
prueba = Prueba()