x = int(input("Entrer un nombre début: "))
y = int(input("Entrer un nombre fin: "))

for i in range(x, y+1):
    if i%2 == 0:
        print(f"{i} est pair")
    elif i%2 == 1:
        print(f"{i} est impair")

print("Fin")