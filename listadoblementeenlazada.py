class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDoble:
    
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamaño = 0


    def esta_vacia(self):
        return self._tamaño == 0

    def __len__(self):
        return self._tamaño


    def agregar_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        
        self._tamaño += 1

    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo
            self._cabeza = nuevo
        
        self._tamaño += 1


    def eliminar_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")

        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente

        if self._cabeza is None:
            self._cola = None
        else:
            self._cabeza.anterior = None

        self._tamaño -= 1
        return dato

    def eliminar_ultimo(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")

        dato = self._cola.dato
        self._cola = self._cola.anterior

        if self._cola is None:
            self._cabeza = None
        else:
            self._cola.siguiente = None

        self._tamaño -= 1
        return dato


    def buscar(self, valor):
        actual = self._cabeza
        while actual:
            if actual.dato == valor:
                return actual
            actual = actual.siguiente
        return None


    def eliminar_nodo(self, nodo):
        if nodo is None:
            return
        
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self._cabeza = nodo.siguiente

        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self._cola = nodo.anterior

        self._tamaño -= 1


    def __iter__(self):
        actual = self._cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def iterar_reversa(self):
        actual = self._cola
        while actual:
            yield actual.dato
            actual = actual.anterior

    def __repr__(self):
        return " <-> ".join(str(x) for x in self)


lista = ListaDoble()

lista.agregar_inicio(5)
lista.agregar_final(10)
lista.agregar_final(20)
lista.agregar_final(30)

print("Lista:", lista)
print("Iteración normal:", list(lista))
print("Iteración inversa:", list(lista.iterar_reversa()))

print("Eliminar primero:", lista.eliminar_primero())
print("Eliminar último:", lista.eliminar_ultimo())

print("Estado final:", lista)
print("Tamaño:", len(lista))