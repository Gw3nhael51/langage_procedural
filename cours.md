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

---

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

