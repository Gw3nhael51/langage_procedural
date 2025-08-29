# Fonction creer_utilisateur
def cree_utilisateur(nom, age, pays="France"):
    print(f"{nom}, is {age} years old and living in {pays}")

if __name__ == '__main__':
    cree_utilisateur("Tom", "22")