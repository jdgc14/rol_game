



class Guild:
    #Clase de los gremios que tambien seran ingresados a nuestros personajes por composicion.
    def __init__(self, id, name, slogan, **kwargs):
        self.id = id
        self.name = name
        self.slogan = slogan
        self.members = []
        for key, value in kwargs.items():
            setattr(self, key, value)

    #Metodo de clase para la creacion de gremios.
    @classmethod
    def create(cls, id, name, slogan, **kwargs):
        return cls(id, name, slogan, **kwargs)

    def read(self):
        self.numbers_of_members = len(self.members)
        print('Guild: {}\n'.format(self.name))
        print('Slogan: {}\n'.format(self.slogan))
        print('Number of members: {}\n'.format(self.numbers_of_members))
        if self.members:
            for member in self.members:
                member.read()
                print()
        