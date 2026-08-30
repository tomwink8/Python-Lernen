# Produktdatenbank
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

produkte = [
    Produkt("Apfel", "Äpfel", 1.99, "der"),
    Produkt("Gurke", "Gurken", 0.99, "die"),
    Produkt("Banane", "Bananen", 2.49, "die")
]


# Warenkorb
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

warenkorb = Warenkorb()

# Funktionen
def zeige_produkte():
    for produkt in produkte:
        print(produkt.beschreibung())

def kaufe_produkt():
    while True:
        produktname = input("Welches Produkt möchtest du kaufen? ")

        for produkt in produkte:
            if produkt.name.lower() == produktname.lower():

                while True:
                    try:
                        menge = int(input("Wie viele möchtest du kaufen? "))

                        if menge > 0:
                            break

                        print("Bitte gib eine Zahl größer als 0 ein.")

                    except ValueError:
                        print("Bittclass Warenkorb:e gib eine gültige Zahl ein.")

                warenkorb.hinzufuegen(produkt, menge)

                if menge == 1:
                    kaufartikel_text = produkt.kaufartikel()
                    print(f"Du hast {kaufartikel_text} {produkt.name} gekauft.")
                else:
                    print(f"Du hast {menge} {produkt.plural} gekauft.")

                return

        print("Produkt nicht gefunden. Verfügbare Produkte:")
        zeige_produkte()

def frage_weiter():
    weiter = "ja"

    while weiter != "nein":
        kaufe_produkt()

        weiter = input("Möchtest du noch etwas kaufen? ").lower()

        while weiter != "ja" and weiter != "nein":
            print('Bitte antworte mit "ja" oder "nein".')
            weiter = input("Möchtest du noch etwas kaufen? ").lower()

def entferne_produkt():
    while True:
        entfernen = input("Möchtest du einen Artikel entfernen? ").lower()

        if entfernen == "nein":
            return

        if entfernen == "ja":
            break

        print('Bitte antworte mit "ja" oder "nein".')

    produktname = input("Welchen Artikel möchtest du entfernen? ")

    if not warenkorb.enthaelt(produktname):
        print(f"{produktname} ist nicht im Warenkorb.")
        return

    while True:
        try:
            menge = int(input("Wie viele möchtest du entfernen? "))

            if menge > 0:
                break

            print("Bitte gib eine Zahl größer als 0 ein.")

        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

    ergebnis = warenkorb.entfernen(produktname, menge)

    if ergebnis is True:
        print(f"{menge}x {produktname} wurde aus dem Warenkorb entfernt.")

    elif ergebnis is False:
        print(f"{produktname} ist nicht im Warenkorb.")

    else:
        print(f"Du hast nur {ergebnis}x {produktname} im Warenkorb.")

# Hauptprogramm
name = input("Wie heißt du? ")

print(f"Hallo {name}!")
print("Ich lerne gerade Python und Git.") 

zeige_produkte()

frage_weiter()

entferne_produkt()

if warenkorb.ist_leer():
    print("\nDer Warenkorb ist leer.")
else:
    warenkorb.zeige_warenkorb()
    print(f"Gesamtpreis: {warenkorb.gesamtpreis():.2f} €")

    
