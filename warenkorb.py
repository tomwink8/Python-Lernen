class WarenkorbArtikel:
    def __init__(self, produkt, menge):
        self.produkt = produkt
        self.menge = menge

    def gesamtpreis(self):
        return self.produkt.preis * self.menge

class Warenkorb:
    def __init__(self):
        self._artikel = []

    def ist_leer(self):
        return len(self._artikel) == 0

    def enthaelt(self, produktname):
        for artikel in self._artikel:
            if artikel.produkt.name.lower() == produktname.lower():
                return True

        return False

    def gesamtpreis(self):
        return sum(artikel.gesamtpreis() for artikel in self._artikel)

    def zeige_warenkorb(self):
        print("\nWarenkorb:")

        for artikel in self._artikel:
            print(
                f"{artikel.menge}x "
                f"{artikel.produkt.name} - "
                f"{artikel.gesamtpreis():.2f} €"
            )

    def hinzufuegen(self, produkt, menge):
        for artikel in self._artikel:
            if artikel.produkt.name == produkt.name:
                artikel.menge += menge
                return

        self._artikel.append(WarenkorbArtikel(produkt, menge))

    def entfernen(self, produktname, menge):
        for artikel in self._artikel:
            if artikel.produkt.name.lower() == produktname.lower():

                if menge > artikel.menge:
                    return artikel.menge

                if menge < artikel.menge:
                    artikel.menge -= menge
                else:
                    self._artikel.remove(artikel)

                return True

        return False