name = input("Wie heißt du? ")

print(f"Hallo {name}!")
print("Ich lerne gerade Python und Git.") 


produkte = [
    {
        "name": "Apfel",
        "preis": 1.99,
        "artikel": "der"
    },
    {
        "name": "Gurke",
        "preis": 0.99,
        "artikel": "die"
    },
    {
        "name": "Banane",
        "preis": 2.49,
        "artikel": "die"
    }
]

def kaufartikel(artikel):
    if artikel == "der":
        return "einen"
    elif artikel == "die":
        return "eine"
    elif artikel == "das":
        return "ein"

def zeige_produkte():
    for produkt in produkte:
        print(f"{produkt['name']}: {produkt['preis']:.2f} €")


zeige_produkte()

def berechne_gesamtpreis():
    gesamtpreis = sum(produkt['preis'] for produkt in produkte)
    return gesamtpreis

gesamtpreis = berechne_gesamtpreis()
print(f"Gesamtpreis: {gesamtpreis:.2f} €")

warenkorb = []

def kaufe_produkt():
    produktname = input("Welches Produkt möchtest du kaufen? ")

    for produkt in produkte:
        if produkt["name"].lower() == produktname.lower():
            warenkorb.append(produkt)

            artikel = kaufartikel(produkt["artikel"])
            print(f"Du hast {artikel} {produkt['name']} für {produkt['preis']:.2f} € gekauft.")
            return

    print("Produkt nicht gefunden.")

weiter = "ja"

while weiter != "nein":
    kaufe_produkt()
    weiter = input("Möchtest du noch etwas kaufen? ").lower()



print("\nWarenkorb:")

for produkt in warenkorb:
    print(f"{produkt['name']} - {produkt['preis']:.2f} €")


def berechne_gesamtpreis():
    gesamtpreis = sum(produkt['preis'] for produkt in warenkorb)
    return gesamtpreis

gesamtpreis = berechne_gesamtpreis()
print(f"Gesamtpreis: {gesamtpreis:.2f} €")