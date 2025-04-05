wagens = []

class Auto:
    def __init__(self, merk, model, jaar):
        self.merk = merk
        self.model = model
        self.jaar = jaar

    def info(self):
        print(f'merk: {self.merk}')
        print(f'model: {self.model}')
        print(f'jaar: {self.jaar}')

class Inventaris:
    def __init__(self, wagens):
        self.wagens = wagens

    def voeg_auto_toe(self, auto):
        self.wagens.append(auto)

    def verwijder_auto(self, auto):
        for wagen in self.wagens:
            if wagen == auto:
                self.wagens.remove(auto)

    def toon_inventaris(self):
        for wagen in wagens:
            print('------------------------------------------------------------------------')
            wagen.info()


auto1 = Auto('Volvo', 'V40', '2018')
auto2 = Auto('Toyota', 'Supra', '2006')
i = Inventaris(wagens)
i.voeg_auto_toe(auto1)
i.voeg_auto_toe(auto2)
i.toon_inventaris()