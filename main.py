name = input("Wie heißt du? ")

print(f"Hallo {name}!")
print("Ich lerne gerade Python und Git.") 


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

#def berechne_gesamtpreis():
    #gesamtpreis = sum(produkt['preis'] for produkt in produkte)
    #return gesamtpreis

#gesamtpreis = berechne_gesamtpreis()
#print(f"Gesamtpreis: {gesamtpreis:.2f} €")

warenkorb = []

def kaufe_produkt():
    produktname = input("Welches Produkt möchtest du kaufen? ")

    for produkt in produkte:
        if produkt["name"].lower() == produktname.lower():

            menge = int(input("Wie viele möchtest du kaufen? "))

            for artikel in warenkorb:
                if artikel["name"] == produkt["name"]:
                    artikel["menge"] += menge

                    if menge == 1:
                        kaufartikel_text = kaufartikel(produkt["artikel"])
                        print(f"Du hast {kaufartikel_text} {produkt['name']} gekauft.")
                    else:
                        print(f"Du hast {menge} weitere {produkt['plural']} gekauft.")

                    return

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

    print("Produkt nicht gefunden.")
            

    

weiter = "ja"

while weiter != "nein":
    kaufe_produkt()

    weiter = input("Möchtest du noch etwas kaufen? ").lower()

    while weiter != "ja" and weiter != "nein":
        print('Bitte antworte mit "ja" oder "nein".')
        weiter = input("Möchtest du noch etwas kaufen? ").lower()



print("\nWarenkorb:")

for produkt in warenkorb:
    gesamt = produkt["preis"] * produkt["menge"]
    print(f"{produkt['menge']}x {produkt['name']} - {gesamt:.2f} €")

    

def berechne_gesamtpreis():

    gesamtpreis = sum(
        produkt["preis"] * produkt["menge"]
        for produkt in warenkorb
    )

    return gesamtpreis

gesamtpreis = berechne_gesamtpreis()
print(f"Gesamtpreis: {gesamtpreis:.2f} €")
    