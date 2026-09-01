class Produkt:
    def __init__(self, name, plural, preis, artikel):
        self.name = name
        self.plural = plural
        self.preis = preis
        self.artikel = artikel

    def kaufartikel(self):
        if self.artikel == "der":
            return "einen"
        elif self.artikel == "die":
            return "eine"
        elif self.artikel == "das":
            return "ein"

    def beschreibung(self):
        return f"{self.name}: {self.preis:.2f} €"