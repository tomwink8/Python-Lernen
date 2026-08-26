# Produktdatenbank
produkte = [
    {
        "name": "Apfel",
        "plural": "Äpfel",
        "preis": 1.99,
        "artikel": "der"
    },
    {
        "name": "Gurke",
        "plural": "Gurken",
        "preis": 0.99,
        "artikel": "die"
    },
    {
        "name": "Banane",
        "plural": "Bananen",
        "preis": 2.49,
        "artikel": "die"
    }
]
# Warenkorb
warenkorb = []

# Funktionen
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

def kaufe_produkt():
    while True:
        produktname = input("Welches Produkt möchtest du kaufen? ")

        for produkt in produkte:
            if produkt["name"].lower() == produktname.lower():

                while True:
                    try:
                        menge = int(input("Wie viele möchtest du kaufen? "))

                        if menge > 0:
                            break

                        print("Bitte gib eine Zahl größer als 0 ein.")

                    except ValueError:
                        print("Bitte gib eine gültige Zahl ein.")

                bereits_im_warenkorb = False

                for artikel in warenkorb:
                    if artikel["name"] == produkt["name"]:
                        artikel["menge"] += menge
                        bereits_im_warenkorb = True
                        break

                if not bereits_im_warenkorb:
                    warenkorb.append({
                        "name": produkt["name"],
                        "plural": produkt["plural"],
                        "preis": produkt["preis"],
                        "artikel": produkt["artikel"],
                        "menge": menge
                    })

                if menge == 1:
                    kaufartikel_text = kaufartikel(produkt["artikel"])
                    print(f"Du hast {kaufartikel_text} {produkt['name']} gekauft.")
                else:
                    print(f"Du hast {menge} {produkt['plural']} gekauft.")

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

def zeige_warenkorb():
    print("\nWarenkorb:")

    for produkt in warenkorb:
        gesamt = produkt["preis"] * produkt["menge"]
        print(f"{produkt['menge']}x {produkt['name']} - {gesamt:.2f} €")

def berechne_gesamtpreis():
    return sum(
        produkt["preis"] * produkt["menge"]
        for produkt in warenkorb
    )


# Hauptprogramm
name = input("Wie heißt du? ")

print(f"Hallo {name}!")
print("Ich lerne gerade Python und Git.") 

zeige_produkte()

frage_weiter()

zeige_warenkorb()

gesamtpreis = berechne_gesamtpreis()
print(f"Gesamtpreis: {gesamtpreis:.2f} €")

    
