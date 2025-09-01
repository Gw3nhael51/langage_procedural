#importer une bibliotheque 
from pathlib import Path

# je stock mon fichier dans une variable via la fonction Path 
fichier = Path("test.txt")
#pareil avec un dossier 
dossier = Path("dossier-vide")

#on vérifie via la méthode exists() si le fichier est disponible
if fichier.exists():
    print("Le fichier est bien disponible :) ")
else:
    print("Fichier non disponible... :( ")

#verifier que "dossier-vide" est un dossier 
print(dossier.is_dir())

#verifier que "dossier-vide" est un dossier 
print(fichier.is_file())


#ouvrir un fichier / et de le fermer à la fin du bloc 
# r -> read only (lecture seul)
# w -> write ecriture => crer ou ecraser un fichier si il existe
# a -> add : ajouter à la fin du fichier sans ecraser le contenu
# x -> creation  : creer un nouveau fichier, erreur si le fichier existe deja 

with open("test.txt", "r", encoding="utf-8") as f:
    #bloc de code à executer sur le fichier...

    #juste lire l'integralité du fichier 
    #content = f.read()
    #print(content)


    #afficher/traiter ligne par ligne
    #for ligne in f :
        #print(ligne.strip())

    #list de lignes
    ligne = f.readlines()     
    print(ligne) 


#automatiquement des que je sors de mon bloc with => le fichier est fermé