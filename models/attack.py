import time


class Attack():
    """
    Esta clase fue creada con el proposito de no repetir todo el tiempo la secuencia de ataque, recibe un daño a realizar,
    y el objetivo de dicho ataque, se modifica el __str__ para que sea amigable con el usuario y le presente de una manera
    legible lo que pasa.
    """
    def __init__(self, damage, target):
        self.damage = damage
        self.target = target
        if self.damage > target.hp:
            self.damage = target.hp
        self.target.hp -= damage

    def __str__(self):
        print(f'{self.damage} damage dealt to {self.target.name}')
        time.sleep(0.5)
        print()
        return f'{self.target.name} has {self.target.hp} HP left'