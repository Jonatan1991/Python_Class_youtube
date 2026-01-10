import random

class Rocola:
    def __init__(self):
        self.tema = [
            "Song 1 - Artist A",
            "Song 2 - Artist B",
            "Song 3 - Artist C",
            "Song 4 - Artist D",
            "Song 5 - Artist E"
        ]
        #queue es la cola de canciones a reproducir
        self.queue = []

    def play(self, k):
        if len(self.queue) >= k:
            primero = self.queue.pop(0)
            self.tema.append(primero)
        indiceRandom = random.randint(0, len(self.tema) - 1)

        tema = self.tema.pop(indiceRandom)
        self.queue.append(tema)
        return tema

rocola = Rocola()
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
print("Reproduciendo:", rocola.play(4), rocola.queue)
