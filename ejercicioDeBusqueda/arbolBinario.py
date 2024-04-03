class ArbolBinario:
    def __init__(self, raiz):
        self.raiz = raiz

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def en_orden(self, nodo):
        if nodo is not None:
            self.en_orden(nodo.izquierda)
            print(nodo.valor)
            self.en_orden(nodo.derecha)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor)
