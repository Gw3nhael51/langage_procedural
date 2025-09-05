### Ajout : Conversions entre Dictionnaires, Listes et Tuples

---

# 🔄 Conversions entre Dictionnaires, Listes et Tuples

## 1. Dictionnaire → Liste

### Récupérer les clés, valeurs ou paires clé-valeur
Un dictionnaire peut être converti en liste en utilisant les méthodes `.keys()`, `.values()` et `.items()`.

```python
voiture = {
    "marque": "Ford",
    "modèle": "Mustang",
    "année": 1964
}

# Convertir les clés en liste
cles = list(voiture.keys())
print(cles)  # ['marque', 'modèle', 'année']

# Convertir les valeurs en liste
valeurs = list(voiture.values())
print(valeurs)  # ['Ford', 'Mustang', 1964]

# Convertir les paires clé-valeur en liste de tuples
paires = list(voiture.items())
print(paires)  # [('marque', 'Ford'), ('modèle', 'Mustang'), ('année', 1964)]
```

---

## 2. Liste → Dictionnaire

### Créer un dictionnaire à partir de deux listes
Si tu as deux listes, une pour les clés et une pour les valeurs, tu peux les combiner pour créer un dictionnaire.

```python
cles = ["marque", "modèle", "année"]
valeurs = ["Ford", "Mustang", 1964]

# Utiliser la fonction zip pour associer les clés et les valeurs
voiture = dict(zip(cles, valeurs))
print(voiture)  # {'marque': 'Ford', 'modèle': 'Mustang', 'année': 1964}
```

---

## 3. Liste → Tuple et Tuple → Liste

### Convertir une liste en tuple
Les tuples sont immuables, ce qui signifie qu'ils ne peuvent pas être modifiés après leur création.

```python
ma_liste = [1, 2, 3, 4]
mon_tuple = tuple(ma_liste)
print(mon_tuple)  # (1, 2, 3, 4)
```

### Convertir un tuple en liste
Pour modifier un tuple, il faut d'abord le convertir en liste.

```python
mon_tuple = (1, 2, 3, 4)
ma_liste = list(mon_tuple)
print(ma_liste)  # [1, 2, 3, 4]
```

---

## 4. Dictionnaire → Tuple et Tuple → Dictionnaire

### Convertir un dictionnaire en tuple de paires clé-valeur
Un dictionnaire peut être converti en tuple de tuples, où chaque tuple est une paire clé-valeur.

```python
voiture = {
    "marque": "Ford",
    "modèle": "Mustang",
    "année": 1964
}

tuple_paires = tuple(voiture.items())
print(tuple_paires)  # (('marque', 'Ford'), ('modèle', 'Mustang'), ('année', 1964))
```

### Convertir un tuple de paires clé-valeur en dictionnaire
Pour convertir un tuple de paires clé-valeur en dictionnaire, utilise la fonction `dict()`.

```python
tuple_paires = (('marque', 'Ford'), ('modèle', 'Mustang'), ('année', 1964))
voiture = dict(tuple_paires)
print(voiture)  # {'marque': 'Ford', 'modèle': 'Mustang', 'année': 1964}
```

---

## 5. Exercices Pratiques

### Exercice 1 : Conversion de Liste en Dictionnaire
Crée une liste de clés et une liste de valeurs, puis convertis-les en dictionnaire.

```python
cles = ["nom", "âge", "ville"]
valeurs = ["Alice", 25, "Paris"]

# Solution
dictionnaire = dict(zip(cles, valeurs))
print(dictionnaire)  # {'nom': 'Alice', 'âge': 25, 'ville': 'Paris'}
```

### Exercice 2 : Conversion de Dictionnaire en Liste de Tuples
Convertis un dictionnaire en une liste de tuples contenant les paires clé-valeur.

```python
etudiant = {
    "nom": "Bob",
    "âge": 22,
    "ville": "Lyon"
}

# Solution
liste_tuples = list(etudiant.items())
print(liste_tuples)  # [('nom', 'Bob'), ('âge', 22), ('ville', 'Lyon')]
```

### Exercice 3 : Conversion de Tuple en Liste
Convertis un tuple en liste pour pouvoir le modifier.

```python
mon_tuple = (10, 20, 30, 40)

# Solution
ma_liste = list(mon_tuple)
print(ma_liste)  # [10, 20, 30, 40]
```

---

# 💡 Conseils pour les Conversions
- **Dictionnaires** : Utilise `.keys()`, `.values()` et `.items()` pour extraire des informations spécifiques.
- **Listes et Tuples** : Utilise `list()` et `tuple()` pour convertir entre ces deux types.
- **Immuabilité** : Les tuples sont immuables, donc convertis-les en listes si tu veux les modifier.

Si tu as d'autres questions ou besoin de plus d'exemples, n'hésite pas à demander ! Bonne révision pour ton DS. 😊