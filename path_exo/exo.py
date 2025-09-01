# Crée un fichier texte notes.txt contenant 5 lignes (par exemple des prénoms + des notes). Ex Bob : 15
# Écris un programme qui :
# Vérifie si le fichier notes.txt existe.

from pathlib import Path

fichier = Path("notes.txt")

if fichier.exists():
    with open(fichier, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
else:
    print("Le fichier notes.txt est introuvable.")


# Si non, affiche : "Le fichier notes.txt est introuvable.«
# •
# Si oui, continue.
# Lis le contenu du fichier de 3 manières différentes :

# Avec read() → affiche tout le contenu en une seule chaîne.
# •
# Avec une boucle for ligne in f → affiche chaque ligne séparément.
# •
# Avec readlines() → affiche la liste des lignes (et par exemple la note du 3e étudiant en utilisant un index).