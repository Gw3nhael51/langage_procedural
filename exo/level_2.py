def main():
    # 13.	: Créer saluer(prenom, message="Bonjour") et tester avec et sans le message.
    name_user = input("Entrez votre prénom: ")

    def saluer(name, message="Bonjour"):
        print(
            f"{message} {name} !"
        )

    saluer(name_user)

    # 14.	 Écrire une fonction somme(*args) qui additionne tous les nombres passés en argument.
    def somme(*args):
        print(f"La somme est: {sum(args)}")

    somme(1, 2, 3, 4, 5, 6, 7, 8, 9)

    # 15.	Créer une fonction infos_personne(**kwargs) et afficher clé : valeur pour chaque élément.
    # 16.	Créer une liste des carrés des nombres pairs de 0 à 20.
    liste = []
    for liste in range(0, 20):
        if liste % 2 == 0:
            print(liste ** 2)

    # 17.	Parcourir un dictionnaire notes = {"Alice": 15, "Bob": 12, "Charlie": 18} et afficher Alice : 15 etc.
    notes = {"Alice": 15, "Bob": 12, "Charlie": 18}
    for note in notes:
        print(f"{note}: {notes[note]}")

    # 18.	Demander une commande (start, stop, pause) et afficher une action correspondante.
    def commande(command):
        match command:
            case "start":
                print("Le programme commence..")
            case "pause":
                print("Le programme est en cours..")
            case "stop":
                print("Le programme est en arrêt..")
            case _:
                print("Commande inconnue")

    commande(command="start")

if __name__ == '__main__':
    main()