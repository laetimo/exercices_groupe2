import random
def home_made_sort (a,b,c):

    list_initiale = [random.randint(a,b) for i in range(c)]
    list_finale = []

    print(list_initiale)


    for y in range(10):
        valeur_max = max(list_initiale)
        list_finale.append(valeur_max)
        list_initiale.remove(valeur_max)
    return list_finale 
        
print(home_made_sort(1, 100, 10))