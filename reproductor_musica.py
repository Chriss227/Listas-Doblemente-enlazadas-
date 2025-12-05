class Nodo:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class Reproductor:
    def __init__(self):
        self.inicio = None

    def agregar(self, song):
        nuevo = Nodo(song)

        if self.inicio is None:
            self.inicio = nuevo
            return

        actual = self.inicio
        while actual.next:
            actual = actual.next
        
        actual.next = nuevo
        nuevo.prev = actual

    def reproducir(self):
        actual = self.inicio

        while True:
            print(f"\nReproduciendo: {actual.song}")
            opcion = input("Escribe 'next', 'prev' o 'salir': ")

            if opcion == "next":
                if actual.next:
                    actual = actual.next
                else:
                    print("No hay siguiente canción.")

            elif opcion == "prev":
                if actual.prev:
                    actual = actual.prev
                else:
                    print("No hay canción anterior.")

            elif opcion == "salir":
                print("Reproductor finalizado.")
                break

            else:
                print("Opción no válida.")

#arranque
player = Reproductor()

player.agregar("song1")
player.agregar("song2")
player.agregar("song3")
player.agregar("song4")

player.reproducir()


