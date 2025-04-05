toppings = []

class Pizza:
    def __init__(self, naam, groote, toppings, kostprijs):
        self.groote = groote
        self.naam = naam
        self.toppings = toppings
        self.kostprijs = kostprijs

    def bereken_prijs(self):
        if self.groote == 'klein':
            self.kostprijs = 8.99
        elif self.groote == 'medium':
            self.kostprijs = 10.99
        else:
            self.kostprijs = 12.99

        for topping in self.toppings:
            self.kostprijs += 150

    def geef_info(self):
        print(f"Naam: {self.naam}")
        print(f"Groote: {self.groote}")
        print(f"Toppings: {self.toppings}")
        pizza1.bereken_prijs()
        print(f'De kostprijs is: {self.kostprijs}')


pizza1 = Pizza("Margherita", "medium", ["kaas", "tomatensaus", "salami"], 0)
pizza1.geef_info()