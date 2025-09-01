def main():
    # LEVEL 1

    # Exo 1
    prenom = input("Quel est votre prenom ?: ")
    print(f"Bonjour {prenom}")

    # Exo 2.	Demander un nombre avec input, puis afficher son double en utilisant int() et float().
    number = int(input("Entrez un nombre x: "))
    print(f"Son double est {number * 2}")

    # Exo 3.	Demander l’âge et afficher "Majeur" ou "Mineur".
    age = int(input("Quel est votre age ?: "))
    if 18 <= age <= 115:
        print("Vous êtes majeur")
    elif age < 18:
        print("Vous êtes mineur")
    else:
        print("Erreur revérifiez votre age")

    # Exo 4.	Vérifier si un nombre est compris entre 10 et 20 inclus.
    x = int(input("Entrez un nombre n: "))
    if 10 <= x <= 20:
        print("Ce nombre est entre 10 & 20")
    else:
        print("Ce nombre n'est pas entre 10 et 20")

    # Exo 5.	Vérifier si un nombre est pair ou impair avec un if en une ligne.

    # Exo 6.	Demander une chaîne et afficher sa première et dernière lettre.

    # Exo 7.	Afficher un nombre avec 2 décimales et centré sur 10 caractères.

    # Exo 8.	Demander un mot de passe jusqu’à ce que l’utilisateur tape "Python".
    while True:
        pass_word = input("Entrez le mot de passe: ").lower()
        if pass_word != "python":
            print("Réessayez")
            continue
        else:
            break
    print("Bienvenue")

    # Exo 9.	Afficher tous les nombres de 1 à 15.
    for i in range(1, 16):
        print(i)

    # Exo 10.	Créer une liste avec les nombres de 1 à 10 et afficher la somme.
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(liste))

    # Exo 11.	: Supprimer les doublons d’une liste [1,2,2,3,3,3,4].
    liste = [1, 2, 2, 3, 3, 3, 4]
    liste = set(liste)
    print(liste)

    # Exo 12.	Créer un dictionnaire {"nom": ..., "age": ...} et afficher les valeurs.
    dictionnaire = {
        "nom": "John",
        "age": "22",
        "ville": "Reims"
    }

    print(f"Nom: {dictionnaire['nom']}, age: {dictionnaire['age']}, ville: {dictionnaire['ville']}")

if __name__ == '__main__':
    main()