class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")

kat = Dier('Kat', "meow")
hond = Dier('Hond', "woof")
koe = Dier('Koe', "moo")

koe.maak_geluid()