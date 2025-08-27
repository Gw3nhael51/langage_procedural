def carnet_contact():
    contact = {
        "nom": input("Entrez votre nom: "),
        "telephone": input("Entrez votre telephone: "),
        "mail": input("Entrez votre mail: ")
    }

    print(" ")
    print("Votre Récapitulatif")
    for i, value in contact.items():
        print(f"{i}: {value}")

if __name__ == '__main__':
    carnet_contact()
