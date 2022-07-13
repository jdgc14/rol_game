import random

#Clases que nuestros tipos de roles heredan por herencia multiple y tendran algunos metodos y atributos extras.

class Sigilo:

    def __init__(self, sigilo=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sigilo = sigilo

    def esconderse(self, nivel_de_luz):
        return self.sigilo and nivel_de_luz < 10


class Agil:

    def __init__(self, agil=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agil = agil

    def evadir(self):
        return self.agil and bool(random.randint(0, 1))

