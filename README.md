# Cours de Python : Langage Procédural

## 🎯 Objectifs

- Comprendre les bases du langage Python
- Mettre en place un environnement de développement, déboguer du code
- Compiler et exécuter des programmes Python

---

## 📝 Variables et Types de Données

### Déclarer une variable

```python
name = "Gwenhael"
```

### Exemple complet avec fonction

```python
name = "GwenGPT"
age = 22

def adult():
    if age >= 18:
        print("je suis majeur")
        return None
    else:
        print("je suis mineur")
        return None

if __name__ == '__main__':
    print(f"Je m\'appelle {name} et j\'ai {age} ans")
    adult()
```

### Conversions de types

```python
age = 22
print(type(age), age)

age = str(age)
print(type(age), age)

age = int(age)
print(type(age), age)

age = bool(age)
print(type(age), age)
```

### Calcul avec saisie utilisateur

```python
nombre1 = input("Saisissez un nombre1: ")
nombre2 = input("Saisissez un nombre2: ")

print(f"Le calcul de {nombre1} * {nombre2} = {int(nombre1) * int(nombre2)}")
```

---

## 🧮 Opérateurs

### Opérateurs d'assignation

```python
import math

number = 3

# number = number + 1
number += 1

# number = number - 3
number -= 3

# number = number * 10
number *= 10

# number = number / 10
number /= 10

# number**2
number **= 2

number1 = 2
number2 = 7.18
number3 = -12

# arrondit
print(round(number2))

# valeur absolue (distance de 0)
print(abs(number3))

# print(pow(number1,number2))

# afficher le nombre le plus grand
print(max(number1, number2, number3))

# afficher le nombre le plus petit
print(min(number1, number2, number3))

# valeur mathematique - importer la librairie math avant
print(math.pi)
print(math.e)
```

---

## 🔀 Conditions

### Condition simple

```python
age = 130

if age <= 0 or age >= 120:
    print(f"age invalide")
elif age > 18:
    print(f"majeur")
else:
    print(f"mineur")

print(f"fin")
```

### Exemple avec conditions ternaires

```python
# correspond à si il n'y a PAS soleil (= false)
if not soleil:
    print("sortez couvert")
else:
    print("prenez vos lunettes de soleil")

# en condition ternaire
# VALEUR SI VRAI IF CONDITION ELSE VALEUR SI FAUX
print("sortez couvert") if not soleil else print("prenez vos lunettes de soleil")
```

---

## 📚 Exercices & Solutions

### Exercice 1 : Calcul de surface et achat

#### Ma solution - Surface du triangle

```python
print("Calculer la surface d\'un triangle")
B = input(f"Quelle est la longueur de votre base: ")  # données en chaine de caracteres
H = input(f"Quelle et la longueur de votre hauteur: ")  # données en chaine de caracteres

# B = int(B)
# H = int(H)

# res = print(B*H/2)
# print(f'La surface de votre triangle est {B} * {H}/2 soit {res} m²')

print(f'La surface de votre triangle est {B} * {H}/2 soit {int(B)* int(H)/2} m²')
```

#### Ma solution - Achat d'article

```python
article = input(f"choisissez un article à acheter: ")
prix = input(f"Quel est son prix?: ")
quantite = input(f"Quel est sa quantite?: ")

print(f"Vous avez acheté {int(quantite)} de {article} au prix total de {int(prix)*int(quantite)}€")
```

---

### Exercice 2 : Calculatrice et gestion des notes

#### Ma solution - Calculatrice avec validation

```python
msg = input(f"Choisissez un opérant: +. Addition , *. Multiplication, -. Soustraction, /. Division: ")

while msg not in ["+", "*", "-", "/"]:
    msg = input("Choisissez un opérant valide: +, *, -, / : ")

a = input("Entrez votre choix nombre a: ")
b = input("Entrez votre choix nombre b: ")

a = int(a)
b = int(b)

if msg == "+":
    print(f"L\'operation {a} + {b} = {a + b}")
elif msg == "*":
    print(f"L\'operation {a} * {b} = {a * b}")
elif msg == "-":
    print(f"L\'operation {a} - {b} = {a - b}")
elif msg == "/":
    if a == 0 or b == 0:
        print("Erreur ne peut pas etre divisé par 0")
        while b == 0:
            b = input("Veuillez choisir un nombre b correct: ")
    else:
        print(f"L\'operation {a} / {b} = {a / b}")
```

#### Ma solution - Gestion des notes

```python
def evaluate_note():
    while True:
        try:
            eval_note = int(input("Mettez votre note (entre 0 et 20) : "))
            if 0 <= eval_note <= 20:
                if 15 < eval_note <= 20:
                    print("Mention très bien")
                elif 10 < eval_note <= 15:
                    print("Mention bien")
                else:
                    print("Mention nulle")
                break
            else:
                print("⚠️ La note doit être comprise entre 0 et 20.")
        except ValueError:
            print("❌ Veuillez entrer un nombre entier valide.")

def sortir():
    while True:
        exit()

def restart():
    while True:
        evaluate_note()
        sortir()

if __name__ == '__main__':
    evaluate_note()
    restart()
```

#### 📋 Correction professeur - Exercice 2.1 (Calculatrice)

```python
# demande de saisie utilisateur
nb1 = input("veuillez saisir un premier nombre ")
nb2 = input("veuillez saisir un 2e nombre ")
operator = input("veuillez saisir un operateur + - * ou /  ")

# conversion en int/float pour faire les calculs
nb1 = float(nb1)
nb2 = float(nb2)

# toute nos verif de "operator" pour savoir quel calcul faire
if operator == "+":
    result = nb1 + nb2
elif operator == "-":
    result = nb1 - nb2
elif operator == "*":
    result = nb1 * nb2
# verifier la /0 on utilise and pour le ET logique (or pour le OU)
elif nb2 == 0 and operator == "/":
    result = "division par 0 impossible"
elif operator == "/":
    result = nb1 / nb2
else:
    result = "operateur incorrect"

print(f"le resultat de {nb1} {operator} {nb2} est de {result}")
```

#### 📋 Correction professeur - Exercice 2.2 (Notes)

```python
note = input("Veuillez saisir une note ")
# convertir en float
note = float(note)
# on verifie la validdité de la note (compris entre 0 et 20)
if note <= 0 or note >= 20:
    res = "note non valide"
elif note < 10:
    res = "insuffisant"
elif note >= 10 and note <= 15:
    res = "bien"
else:
    res = "tres bien"
# on affiche le resultat
print(res)
```

---

### Exercice 3 : Validation de pseudo

#### Ma solution - Validation avec boucles

```python
def verification():
    while True:
        user_name = input("Entrez votre prénom : ").lower().replace(" ", "")

        if not user_name.isalpha():
            print("❌ Le nom ne doit contenir que des lettres.")
            continue

        if len(user_name) > 12:
            print(f"❌ Entrée non validée : {len(user_name)} caractères (max 12)")
            continue

        print(f"✅ Entrée validée : {len(user_name)} caractères")
        break

if __name__ == '__main__':
    verification()
```

#### 📋 Correction professeur - Version 1

```python
pseudo = input("veuillez saisir un pseudo")

if len(pseudo) < 12 and pseudo.count(" ") == 0 and pseudo.isalpha():
    print("pseudo validée")
else:
    print("pseudo non valide")
```

#### 📋 Correction professeur - Version regex

```python
import re

pseudo = input("veuillez saisir un pseudo")

# ^ : debut de la chaine
# [A-Za-z] n'importe quel lettre maj ou min de a à z
# {1,11} : longueur entre 1 et 11
# $ fin de la chaine
pattern = "^[A-Za-z]{1,11}$"

if re.match(pattern, pseudo):
    print("pseudo validée")
else:
    print("pseudo non valide")
```

---

### Exercice 4 : Jeu de devinette

#### Ma solution - Jeu avec match/case

```python
import random

number = random.randint(0, 100)
essai = 0

while True:
    essai += 1
    try:
        guess_number = int(input("Trouvez le chiffre: "))
        if guess_number < number:
            print("C'est plus")
        elif guess_number > number:
            print("C'est moins")
        else:
            print("Vous avez trouvé 🤗")
            print(f"En {essai} tentatives !")

            match essai:
                case 1:
                    message = "Incroyable ! Premier coup, tu es un génie 🔥"
                case 2 | 3:
                    message = "Rapide et efficace, tu ne traînes pas 💨"
                case 4 | 5 | 6:
                    message = "Belle performance, tu tiens le rythme 💪"
                case 7 | 8 | 9 | 10:
                    message = "Tu t'accroches bien, la victoire est proche 👀"
                case 11 | 12 | 13 | 14 | 15:
                    message = "On commence à transpirer un peu 😅"
                case 16 | 17 | 18 | 19 | 20:
                    message = "Tu refuses d’abandonner, j’admire ta ténacité 🧗"
                case _ if 21 <= essai <= 30:
                    message = "Courage… le bon nombre est quelque part là-dedans 🕵️"
                case _ if 31 <= essai <= 50:
                    message = "Tu explores toutes les possibilités… méthodique ! 🧮"
                case _:
                    message = "Tu mérites une médaille pour ta persévérance 🏅"
            print(message)

            break
    except ValueError:
        print("❌ Essayez un nombre valide")

```

#### 📋 Correction professeur - Exercice 4

```python
chaine = input("Entrez une chaine de caractères")
chaine = chaine[:-3]

print(chaine)
```

## Boucle While et boucle For

```python 
number = int(input("Entrer un nombre: "))

while number < 0:
    number = int(input("Entrer un nombre: "))
    continue

if number != 0:
    for i in range(number,0,-1):
        print(i)

for x in range(100,0,-1):
    print("💥💥💥🧨🧨🧨🧨🧨🧨🧨")
```

---

```python 
x = int(input("Entrer un nombre début: "))
y = int(input("Entrer un nombre fin: "))

for i in range(x, y+1):
    if i%2 == 0:
        print(f"{i} est pair")
    elif i%2 == 1:
        print(f"{i} est impair")

print("Fin")
```

## Dictionnaires

```python
voiture = {
  "marque": "Ford",
  "modele": "Mustang",
  "annee": 1964
}

# print(voiture["brand"], voiture["model"], voiture["year"])

for i in voiture:
    print(i, voiture[i])
print("Fin")
print(" ")

for key, value in voiture.items():
    print(f"clé: {key}: ,{value}")
```

```python 
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

```
```python
eleve = {
    "benoit": "15",
    "kevin": "5",
    "lucas": "10"
}

search_student = input("Recherchez un étudiant: ").lower()

if search_student in eleve:
    print(f"La note de {search_student} est de {eleve[search_student]}")
else:
    print("Eleve inconnu")
```
## Les listes

```python
prenoms = ["Bob","Tom","Sarah"]

print(prenoms)


#afficher l'index premiere position commence à 0
print(prenoms[0])

#afficher la valeur du dernier element (-1)
print(prenoms[-1])

#parcourir le tableau avec une boule for
for prenom in prenoms:
    print(prenom)

#longueur d'un tableau => fonction len(list)
print (len(prenoms))

#ajouter un element à la fin de la list => append
prenoms.append("Toto")

#ajouter un element x à l'index i =>insert(i,x)
prenoms.insert(0,"Titi")
print(prenoms)

#supprimer le dernier element
prenoms.pop()
print(prenoms)

#supprimer la premiere occurence de x => methode remove(x)
prenoms.remove("Bob")
print(prenoms)
```
```python
#Creer une list de notes avec les valeurs : 12, 15, 8, 19, 10

notes = [12, 15, 8, 19, 10]

# 1. afficher la note la plus elevé max(list) et la plus basse min(list)
print("Note la plus élevée", max(notes))
print("Note la plus basse", min(notes))

# 2. Calculer et afficher la moyenne (soit en utilisant for soit avec une fonction)
#avec la fonction sum
print(sum(notes)/len(notes))

#version avec une boucle
somme = 0
for note in notes:
    somme += note
moyenne =  somme/len(notes)

print(f"la moyenne est de {moyenne} ")

# 3. ajouter une nouvelle note en fin de tableau et afficher le tableau final
notes.append(13)
print(notes)
```

```python
#declarer un ensemble
animals = {"oiseau", " chat", "chien"}

print(animals)

#LIST DE METHODES UTILES

#ajouter un element : methode add(element)
animals.add("castor")
print(animals)


#suppr un element : methode remove(element)
animals.remove("castor")
print(animals)

#verifie si une vbaleur est presente dans un set
print("chien" in animals)
print("castor" in animals)


#OPERATIONS 
notesA = {1,2,3,4}
notesB = {3,4,5,6}

#Union de A et B (rassemble les 2 et elimine les doublons) |
print (notesA | notesB)

#Intersection de A et B (rassemble les elements en commun uniquemeent et elimine les doublons) &
print (notesA & notesB)

#Difference de A et B -
print (notesA - notesB)

#Difference exclusif : ^
print (notesA ^ notesB)
```

## Exercice:

```python
# Liste de mots interdits
liste = ["spam", "arnaque", "escroquerie"]

# Demande à l’utilisateur de saisir un message
msg = input("Entrez un message : ").lower().split(" ")

# Vérifie si un mot interdit est présent
bad_word = False
for mot in liste:
    if mot in msg:
        bad_word = True
        break

# Affiche le résultat
if bad_word:
    print("Message rejeté")
else:
    print("Message accepté")

```

##Correction: 

```python

# 1. Demande à l'utilisateur de saisir plusieurs prénoms, séparés par des virgules.
# Exemple: "Alice,Bob,Alice,Tom,Bob«
noms = input("saisir plusieurs noms séparées par des ',' ")
tableauNoms = noms.split(",")

# Transforme la chaîne en liste avec .split(',').

# Convertis la liste en set pour éliminer les doublons.Affichele set obtenu.
listNoms = set(tableauNoms)

print(listNoms)

# 2. Crée deux sets :
groupe_a= {"Alice", "Bob", "Claire"}
groupe_b= {"Claire", "David", "Emma"}
# Affiche :Les personnes dans les deux groupes.
print(groupe_a & groupe_b)

# Les personnes unique a chaque groupe 
print(groupe_a - groupe_b)

# union des 2 listes sans doublons
print(groupe_a | groupe_b)


# 3. Crée une liste de mots interdits : ["spam", "arnaque", "escroquerie"].
# Demande à l’utilisateur de saisir un message.
# Si un mot interdit est trouvé dans le message, affiche "Message rejeté", 
# sinon "Message accepté".
# Astuce : utiliser une boucle + in.*/

motsInterdit ={"spam", "arnaque","escroquerie"}

message = input("veuillez saisir une phrase : ")

#on convertir de str (minuscule) -> list -> set
mots_message = set(message.lower().split(" "))

#verifier avec une intersection
if mots_message & motsInterdit:
    print("message non valide")
else:
    print("messsage valide")
```
## Exercice
```python
#Gestion d'un club de sport : Gerer les adhérents et leur informations

# choisir quand utiliser une liste, un dictionnaire, ou un ensemble pour chaque partie du problème

#1. Stocker les prénoms des adhérents "Bob", "Toto", "Tata", "Titi", "Bob" (Bob s'est inscrit 2 fois...)
#Liste car doublons
adherent = ["Bob", "Toto", "Tata", "Titi", "Bob"]

#  Afficher la liste des adhérents

print(f"Liste des adhérents actuels: \n")
for ad in adherent:
    print(f"{ad}")

# 2. Supprimer les doublons et afficher la liste finale*
adherent = set(adherent)

print(f"Nouvelle liste des adhérents: \n")


# 3. Pour chaque adhérent on veut stocker son âge et son sport préféré
infos = {
    "Bob": {"age": 25, "sport": "hockey"},
    "Toto": {"age": 28, "sport": "rugby"}
}

# afficher l'age de Bob

print(f"Age de Bob: {infos['Bob']['age']}, sport favori {infos['Bob']['sport']} ")

# changer son sport favori en "tennis"


#4. Rechercher :
# ajouter un adhérent "David" sport "natation"
```


## Correction
```python
#Gestion d'un club de sport : Gerer les adhérents et leur informations 

# choisir quand utiliser une liste, un dictionnaire, ou un ensemble pour chaque partie du problème

#1. Stocker les prénoms des adhérents "Bob", "Toto", "Tata", "Titi", "Bob" (Bob s'est inscrit 2 fois...)
#  Afficher la liste des adhérents dans l'ordre

#ici on veut autoriser les doublons, l'ordre d'inscription peut etre important => list 
adherents=["Bob", "Toto", "Tata", "Titi", "Bob"]
print (f"Liste initiale : {adherents}")


# 2. Supprimer les doublons et afficher la liste finale 
#on ne veut pas de doublons => set
adherents_unique = set(adherents)
print(adherents_unique)

# 3. Pour chaque adhérent on veut stocker son âge et son sport préféré
#on veut stocker des données ordonnées pour chaque adherent => dictionnaire (de dictionnaire)

infos_adherent = {
    "Bob" : {"age" : 25, "sport" : "hockey"},
    "Toto" : {"age" : 45, "sport" : "majong"}
}

#4. Rechercher :
# afficher l'age de Bob
print("Age de bob : ", infos_adherent["Bob"]["age"])
# changer son sport favori en "tennis"
infos_adherent["Bob"]["sport"] = "tennis" 
print("nouveau sport de bob : ", infos_adherent["Bob"]["sport"])
# ajouter un adhérent "David" sport "natation"
infos_adherent["David"] = {"age" : 72, "sport" : "natation"}

#afficher les infos de David
print(infos_adherent["David"])
```
## Exercice bibliothèque

```python
#Gestion d'une bibliotheque

# 1. Creer un "ensemble de données " qui contient les livres de la bibliotheque (peut afficher les doublons )
bob = {
    "library": ["Harry Potter", "Le python pour les nuls", "PHP pour les nuls", "Naruto", "Harry Potter"]
}

# 2. choisir un " ensemble de données " qui n'affiche que les titres uniques
print("Livres empruntés par Bob: \n")
for book in set(bob["library"]):
    print("-", book)
print("\n")

# 3. choisir un "ensemble de données " qui associe un livre a un adherent ayant emprunté

alice = {
    "library": ["python", "R"]
}

tom = {
    "library": ["tomtom & nana", "titin", "garfield"]
}

emprunts = {
    "bob": bob["library"],
    "alice": alice["library"],
    "tom": tom["library"]
}

# 4. Recherche quel livre "Bob" a emprunté (via get par exemple)
print(f"Bob a emprunté: {bob.get('library')} \n")

# 5. Modifier le livre de "Bob" en "S'incrire a un club pour les nuls"
print(bob["library"].append("S\'inscrire à un club pour les nuls \n"))

# 6. Ajouter un nouveau lecteur "David" qui emprunte "LSDA" (soit via clé soit via update)
emprunts['David'] = ["Le Seigneur Des Anneaux \n"]

# 7. Supprimer un lecteur (del)
del emprunts["alice"]

#8.Afficher la liste finale
print("Liste finale")
for emprunt in emprunts.items():
    print(emprunt)

```

## Correction exo bibliothèque
```python
#Exercice : gestion d'une bibliothèque 

# 1. Creer un "ensemble de données " qui contient les livres de la bibliotheque (peut afficher les doublons )
livres_list = ["Harry Potter", "Le rouge & le noir", "Le petit prince", "Harry Potter"]
print(f"Liste initale : {livres_list}")

# 2. choisir un " ensemble de données " qui n'affiche que les titre unique 
livres_unique = set(livres_list)
print(f"Liste initale : {livres_unique}")


# 3. choisir un "ensemble de données " qui associe un livre a un adherent ayant emprunté
lecteurs = {
    "Tom" : "Harry Potter",
    "Bob" : "Le petit prince",
    "Sarah" : "le rouge & le noir"
}


# 4. Recherche quel livre "Bob" a emprunté (via get par exemple )
#via get => gere le cas ou la clé n'existe pas
print(lecteurs.get("Bob"))

#via l'accès direct
print(lecteurs["Bob"])

# 5. Modifier le livre de "Bob" en "S'incrire a un club pour les nuls" (soit via clé soit via update)
lecteurs["Bob"] = "S'isncrire à un club pour les nuls"

#avec update => pratique si on veut modifier ou ajouter plusieurs clés 
lecteurs.update({"Bob" : "S'inscrire à un club pour les nuls"})

# 6. Ajouter un nouveau lecteur "David" qui emprunte "LSDA" 

#via l'accès direct
lecteurs["David"] = "Le seigneur des anneaux"

#avec update (sert aussi à ajouter)
lecteurs.update({"David": "Le seigneur des anneaux"})


# 7. Supprimer un lecteur (del)
del lecteurs["Tom"]


# 8. Afficher la liste finale
for nom, livre in lecteurs.items():
    print(f"{nom} a emprunté {livre}")
```

---

## Exercice entrée de notes

```python
# Fonction pour saisir les notes
def saisir_notes():
    notes = []

    while True:
        try:
            note = int(input("Entrez une note (ou -1 pour terminer) : "))
            if note == -1:
                break
            elif 0 <= note <= 20:
                notes.append(note)
            else:
                print("Veuillez entrer une note entre 0 et 20.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
    return notes


# Fonction pour calculer la moyenne
def calculer_moyenne(notes):
    if notes:
        return sum(notes) / len(notes)
    else:
        return None


# Crée une fonction afficher_resultat(moyenne) qui affiche un message formaté :

def afficher_resultat(moyenne):
    if moyenne is None:
        print("Aucune note saisie.")
    elif moyenne >= 16:
        print("Très bien")
    elif moyenne >= 14:
        print("Bien")
    elif moyenne >= 12:
        print("Assez bien")
    elif moyenne >= 10:
        print("Passable")
    else:
        print("Insuffisant")


if __name__ == '__main__':
    notes = saisir_notes()
    print(f"\n Voici les notes : {notes}")

    moyenne = calculer_moyenne(notes)
    print(f"\n Voici la moyenne : {moyenne}")

    print(f"Mention: {afficher_resultat(moyenne)}")

```

## Correction:

```python
# EXERCICE LISTE DE NOTES

# Crée une fonction saisir_notes() qui demande à l’utilisateur d’entrer plusieurs notes 
# (saisie terminée quand l’utilisateur tape -1). La fonction renvoie la liste des notes.

def saisirNote():
    notes = []
    note = 0

    #tant que la saisie n'est pas -1 on continue de demander la saisie et d'alimenter(append) la list
    while note != -1:
        note = float(input("Entrez une note, ou -1 pour terminer la saisie"))
        #empeche que -1 rentre dans le tableau 
        if note != -1:
            notes.append(note)
    #la fonction renvoi le tableau de notes
    return notes


# Crée une fonction moyenne(notes) qui reçoit une liste de notes et renvoie la moyenne.
# verifier que le tableau n'est pas vide 

def moyenne(notes):
    if len(notes) != 0:
        res = sum(notes) / len(notes)
    else:
        res = "tableau vide..."
    return res




# Crée une fonction afficher_resultat(moyenne) 
# qui affiche un message formaté :"Très bien" si la moyenne ≥ 16
# "Bien" si la moyenne ≥ 14
# "Assez bien" si la moyenne ≥ 12
# "Passable" si la moyenne ≥ 10
# "Insuffisant" sinon

def afficher_resultat(moyenne):
    if moyenne >= 16:
        print(f"Moyenne {moyenne} est très bien")
    elif moyenne >= 14:
        print(f"Moyenne {moyenne} est bien")    
    elif moyenne >= 12:
        print(f"Moyenne {moyenne} est assez bien") 
    elif moyenne >= 10:
        print(f"Moyenne {moyenne} est passable")
    else:
        print(f"Moyenne {moyenne} est insuffisant")
        


# Dans le programme principal :
#Appeler saisir_notes()
notes = saisirNote()

#Calculer la moyenne avec moyenne()
moy = moyenne(notes)

#Afficher le résultat avec afficher_resultat()
afficher_resultat(moy)
```
---
```python

#definir une fonction sans parametre
def sayHello():
    print("Hello")

#definir une fonction sans parametre
def sayHelloName(firstname, name):
    print(f"Hello {firstname} {name}")

#meme principe avec un return 
def multiply(x,y):
    return (x*y)

#fonction avec valeur par defaut (ici age)
def sayHelloName(firstname, name, age = 12):
    print(f"Bonjour {firstname} {name}, tu as {age} ans")


#les appeler
sayHello()
sayHelloName("Tim", "Dupont")

#appel de fonction avec keywords
sayHelloName(name = "Dupont", firstname="Dupont")

print(multiply(2,3))
```

## Exercice:
```python
# Fonction creer_utilisateur
def cree_utilisateur(nom, age, pays="France"):
    print(f"{nom}, is {age} years old and living in {pays}")

if __name__ == '__main__':
    cree_utilisateur("Tom", "22")
```

## Correction:

```python

```

## 📖 Notes Importantes

### Opérateurs logiques

- `and` : ET logique
- `or` : OU logique
- `not` : NON logique

### Méthodes utiles pour les chaînes

- `.isalpha()` : vérifie si tous les caractères sont des lettres
- `.count()` : compte le nombre d'occurrences
- `len()` : longueur de la chaîne
- `.lower()` : convertit en minuscules
- `.replace()` : remplace des caractères

### Gestion des erreurs

- `try/except` : pour capturer et gérer les erreurs
- `ValueError` : erreur de conversion de type

### Expressions régulières (regex)

- Module `re` pour la validation avancée de chaînes
- Patterns pour définir des formats précis

