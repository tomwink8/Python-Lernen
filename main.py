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
        self.artikel = []

    def gesamtpreis(self):
        return sum(artikel.gesamtpreis() for artikel in self.artikel)

    def zeige_warenkorb(self):
        print("\nWarenkorb:")

        for artikel in self.artikel:
            print(
                f"{artikel.menge}x "
                f"{artikel.produkt.name} - "
                f"{artikel.gesamtpreis():.2f} €"
            )

    def hinzufuegen(self, produkt, menge):
        for artikel in self.artikel:
            if artikel.produkt.name == produkt.name:
                artikel.menge += menge
                return

        self.artikel.append(WarenkorbArtikel(produkt, menge))

    def entfernen(self, produktname):
        for artikel in self.artikel:
            if artikel.produkt.name.lower() == produktname.lower():
                self.artikel.remove(artikel)
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
                        print("Bitte gib eine gültige Zahl ein.")

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
    produktname = input("Welchen Artikel möchtest du entfernen? ")

    if warenkorb.entfernen(produktname):
        print(f"{produktname} wurde aus dem Warenkorb entfernt.")
    else:
        print(f"{produktname} ist nicht im Warenkorb.")

# Hauptprogramm
name = input("Wie heißt du? ")

print(f"Hallo {name}!")
print("Ich lerne gerade Python und Git.") 

zeige_produkte()

frage_weiter()

entferne_produkt()

warenkorb.zeige_warenkorb()

gesamtpreis = warenkorb.gesamtpreis()
print(f"Gesamtpreis: {gesamtpreis:.2f} €")

    
