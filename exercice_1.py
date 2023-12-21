#---------------------Ce à quoi j'ai pensé-------------------------#
valeur_a = 20
valeur_b = 40
number = valeur_a
liste = [] # je déclare une liste vide afin de l'alimenter par la suite.

while valeur_a < valeur_b: # la boucle while va permettre de créer une liste avec un chiffre + 1 à chaque itération. 
    number += 1
    liste.append(number)
    valeur_a += 1
    print(number)

print(liste)

for x in liste: # la boucle for va me permettre d'effacer les paires de la liste. Elle vérifie si les nombres (x), une fois divisé par 2, n'ont pas de reste après la virgule
    if x % 2 == 0:
        liste.remove(x)
print(liste)

liste = str(liste).replace("[", "").replace("]", "").replace(",", "") # on transforme la liste int en string pour pouvoir remplacer les ' [ ] ' et les ',' par du vide.

print(liste)



