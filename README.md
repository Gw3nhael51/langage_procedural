# prises de notes + cours généré

# 🎯 Objectifs du Cours
- Comprendre les bases du langage Python.
- Savoir mettre en place un environnement de développement et déboguer du code.
- Compiler et exécuter des programmes Python.

---

# 📝 Variables et Types de Données

## Déclaration de variables
```python
name = "Gwenhael"
age = 22
```

## Exemple complet avec fonction
```python
def adult():
    if age >= 18:
        print("Je suis majeur")
    else:
        print("Je suis mineur")

if __name__ == '__main__':
    print(f"Je m'appelle {name} et j'ai {age} ans")
    adult()
```

## Conversions de types
```python
age = 22
print(type(age), age)  # <class 'int'> 22
age = str(age)
print(type(age), age)  # <class 'str'> '22'
age = int(age)
print(type(age), age)  # <class 'int'> 22
age = bool(age)
print(type(age), age)  # <class 'bool'> True
```

## Calcul avec saisie utilisateur
```python
nombre1 = input("Saisissez un nombre1: ")
nombre2 = input("Saisissez un nombre2: ")
print(f"Le calcul de {nombre1} * {nombre2} = {int(nombre1) * int(nombre2)}")
```

---

# 🧮 Opérateurs

## Opérateurs d'assignation
```python
import math

number = 3
number += 1  # number = 4
number -= 3  # number = 1
number *= 10  # number = 10
number /= 10  # number = 1.0
number **= 2  # number = 1.0

number1 = 2
number2 = 7.18
number3 = -12

print(round(number2))  # 7
print(abs(number3))  # 12
print(max(number1, number2, number3))  # 7.18
print(min(number1, number2, number3))  # -12
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
```

---

# 🔀 Conditions

## Condition simple
```python
age = 130
if age <= 0 or age >= 120:
    print("Âge invalide")
elif age > 18:
    print("Majeur")
else:
    print("Mineur")
print("Fin")
```

## Condition ternaire
```python
soleil = False
print("Sortez couvert") if not soleil else print("Prenez vos lunettes de soleil")
```

---

# 📚 Exercices et Solutions

## Exercice 1 : Calcul de surface et achat

### Surface du triangle
```python
B = input("Longueur de la base : ")
H = input("Longueur de la hauteur : ")
print(f"La surface de votre triangle est {int(B) * int(H) / 2} m²")
```

### Achat d'article
```python
article = input("Choisissez un article : ")
prix = input("Prix de l'article : ")
quantite = input("Quantité : ")
print(f"Vous avez acheté {int(quantite)} {article} pour un total de {int(prix) * int(quantite)}€")
```

---

## Exercice 2 : Calculatrice et gestion des notes

### Calculatrice avec validation
```python
msg = input("Choisissez un opérateur (+, *, -, /) : ")
while msg not in ["+", "*", "-", "/"]:
    msg = input("Opérateur invalide. Choisissez (+, *, -, /) : ")

a = int(input("Nombre a : "))
b = int(input("Nombre b : "))

if msg == "+":
    print(f"{a} + {b} = {a + b}")
elif msg == "*":
    print(f"{a} * {b} = {a * b}")
elif msg == "-":
    print(f"{a} - {b} = {a - b}")
elif msg == "/":
    if b == 0:
        print("Erreur : division par zéro")
    else:
        print(f"{a} / {b} = {a / b}")
```

### Gestion des notes
```python
def evaluate_note():
    while True:
        try:
            eval_note = int(input("Note (entre 0 et 20) : "))
            if 0 <= eval_note <= 20:
                if eval_note > 15:
                    print("Très bien")
                elif eval_note > 10:
                    print("Bien")
                else:
                    print("Nul")
                break
            else:
                print("Note invalide. Doit être entre 0 et 20.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

evaluate_note()
```

---

## Exercice 3 : Validation de pseudo

### Solution avec boucles
```python
def verification():
    while True:
        user_name = input("Prénom : ").lower().replace(" ", "")
        if not user_name.isalpha():
            print("Le nom ne doit contenir que des lettres.")
        elif len(user_name) > 12:
            print(f"Trop long : {len(user_name)} caractères (max 12).")
        else:
            print(f"Entrée validée : {len(user_name)} caractères")
            break

verification()
```

### Correction avec regex
```python
import re

pseudo = input("Saisir un pseudo : ")
pattern = "^[A-Za-z]{1,11}$"
if re.match(pattern, pseudo):
    print("Pseudo valide")
else:
    print("Pseudo invalide")
```

---

## Exercice 4 : Jeu de devinette

### Solution avec `match/case`
```python
import random

number = random.randint(0, 100)
essai = 0

while True:
    essai += 1
    try:
        guess_number = int(input("Devinez le nombre : "))
        if guess_number < number:
            print("C'est plus")
        elif guess_number > number:
            print("C'est moins")
        else:
            print(f"Bravo ! Vous avez trouvé en {essai} tentatives.")
            match essai:
                case 1:
                    print("Incroyable ! Premier coup, tu es un génie 🔥")
                case 2 | 3:
                    print("Rapide et efficace 💨")
                case _ if essai <= 6:
                    print("Belle performance 💪")
                case _ if essai <= 10:
                    print("Tu t'accroches bien 👀")
                case _ if essai <= 20:
                    print("Tu refuses d'abandonner 🧗")
                case _:
                    print("Tu mérites une médaille pour ta persévérance 🏅")
            break
    except ValueError:
        print("Entrée invalide. Essayez un nombre.")
```

---

# 🔄 Boucles

## Boucle `while` et `for`
```python
# Exemple avec `while`
number = int(input("Entrez un nombre positif : "))
while number < 0:
    number = int(input("Erreur. Entrez un nombre positif : "))

# Exemple avec `for`
for i in range(number, 0, -1):
    print(i)

# Afficher les nombres pairs et impairs
x = int(input("Début : "))
y = int(input("Fin : "))
for i in range(x, y + 1):
    if i % 2 == 0:
        print(f"{i} est pair")
    else:
        print(f"{i} est impair")
```

---

# 📋 Dictionnaires

## Exemple de dictionnaire
```python
voiture = {
    "marque": "Ford",
    "modèle": "Mustang",
    "année": 1964
}

for key, value in voiture.items():
    print(f"{key} : {value}")
```

## Carnet de contacts
```python
def carnet_contact():
    contact = {
        "nom": input("Nom : "),
        "téléphone": input("Téléphone : "),
        "mail": input("Mail : ")
    }
    print("\nRécapitulatif :")
    for key, value in contact.items():
        print(f"{key} : {value}")

carnet_contact()
```

---

# 📌 Listes

## Manipulation de listes
```python
prenoms = ["Bob", "Tom", "Sarah"]
print(prenoms[0])  # Bob
print(prenoms[-1])  # Sarah

prenoms.append("Toto")
prenoms.insert(0, "Titi")
print(prenoms)  # ['Titi', 'Bob', 'Tom', 'Sarah', 'Toto']

prenoms.pop()  # Supprime 'Toto'
prenoms.remove("Bob")  # Supprime 'Bob'
print(prenoms)  # ['Titi', 'Tom', 'Sarah']
```

## Exercice : Liste de notes
```python
notes = [12, 15, 8, 19, 10]
print("Note la plus élevée :", max(notes))
print("Note la plus basse :", min(notes))
print("Moyenne :", sum(notes) / len(notes))
```

---

# 🧩 Ensembles (`set`)

## Opérations sur les ensembles
```python
animals = {"oiseau", "chat", "chien"}
animals.add("castor")
animals.remove("castor")
print("chien" in animals)  # True

notesA = {1, 2, 3, 4}
notesB = {3, 4, 5, 6}
print(notesA | notesB)  # Union : {1, 2, 3, 4, 5, 6}
print(notesA & notesB)  # Intersection : {3, 4}
print(notesA - notesB)  # Différence : {1, 2}
print(notesA ^ notesB)  # Différence exclusive : {1, 2, 5, 6}
```

---

# 📝 Exercices Supplémentaires

## Gestion d'un club de sport
```python
adherents = ["Bob", "Toto", "Tata", "Titi", "Bob"]
adherents_unique = set(adherents)
print("Liste sans doublons :", adherents_unique)

infos_adherent = {
    "Bob": {"âge": 25, "sport": "hockey"},
    "Toto": {"âge": 45, "sport": "mahjong"}
}

infos_adherent["Bob"]["sport"] = "tennis"
infos_adherent["David"] = {"âge": 72, "sport": "natation"}
print("Sport de Bob :", infos_adherent["Bob"]["sport"])
print("Infos de David :", infos_adherent["David"])
```

---

# 📖 Notes Importantes

## Opérateurs logiques
- `and` : ET logique
- `or` : OU logique
- `not` : NON logique

## Méthodes utiles pour les chaînes
- `.isalpha()` : Vérifie si tous les caractères sont des lettres.
- `.count()` : Compte le nombre d'occurrences.
- `len()` : Longueur de la chaîne.
- `.lower()` : Convertit en minuscules.
- `.replace()` : Remplace des caractères.

## Gestion des erreurs
- `try/except` : Capture et gère les erreurs.
- `ValueError` : Erreur de conversion de type.

## Expressions régulières
- Module `re` pour la validation avancée de chaînes.
- Patterns pour définir des formats précis.

---

# 🎯 Exercices Bonus

## Liste de compréhension
```python
prenoms = ["Shahed", "Cedric", "GwenGPT", "Babou"]
majuscules = [prenom.upper() for prenom in prenoms if prenom == "Shahed"]
print(majuscules)  # ['SHAHED']
```

## Table de multiplication
```python
table_multip = [x * y for x in range(1, 10) for y in range(1, 10)]
print(table_multip)
```

---

# 💡 Conseils pour le DS
- **Relis les exercices** : Assure-toi de bien comprendre chaque étape.
- **Pratique les boucles et conditions** : Ce sont des éléments clés.
- **Gère les erreurs** : Utilise `try/except` pour éviter les plantages.
- **Utilise des fonctions** : Pour structurer ton code et le rendre réutilisable.

Bonne chance pour ton DS, Gwenhael ! Si tu as des questions ou besoin de précisions sur un point, n'hésite pas à demander. 😊