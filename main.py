name = input("Wie heißt du? ")

print(f"Hallo {name}!")
print("Ich lerne gerade Python und Git.") 


produkte = [
    {
        "name": "Apfel",
        "preis": 1.99
    },
     {
        "name": "Gurke",
        "preis": 0.99
    },
    {
        "name": "Banane",
        "preis": 2.49
    }
]


def zeige_produkte():
    for produkt in produkte:
        print(f"{produkt['name']}: {produkt['preis']:.2f} €")


zeige_produkte()