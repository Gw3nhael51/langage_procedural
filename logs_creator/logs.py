from pathlib import Path
from datetime import datetime

# Obtenir la date et l'heure actuelles
now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(now)

# Définir le chemin du fichier
file = Path("logs.txt")

# Demander à l’utilisateur d’entrer une phrase (ou "quit" pour arrêter)
user_entry = input("Entrez votre message (ou 'quit' pour arrêter): ")

# Si l'utilisateur veut quitter, on termine le programme
while user_entry != "quit":
    # Si le fichier existe, on ajoute le message
    if file.exists():
        with file.open("a", encoding="utf-8") as f:
            f.write(f"{now} : {user_entry}\n")
    else:
        # Si le fichier n'existe pas, on le crée et on écrit le message
        with file.open("w", encoding="utf-8") as f:
            f.write(f"{now} : {user_entry}\n")
    print("Message enregistré.")
