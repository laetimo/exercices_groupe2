import random as rn
# def home_made_sort (a,b,c):

#     list_initiale = [random.randint(a,b) for i in range(c)]
#     list_finale = []

#     print(list_initiale)


#     for y in range(10):
#         valeur_max = max(list_initiale)
#         list_finale.append(valeur_max)
#         list_initiale.remove(valeur_max)
#     return list_finale 

# print(home_made_sort(1, 100, 10))

list_not_sorted = [2,1,5,3,4,3]
#list_not_sorted = [rn.randint(5,20) for i in range (10)]
print(list_not_sorted)
n = len(list_not_sorted)
print(n)
#list_sorted = []

def sort_my_list(list) :
    liste = [list_not_sorted[0]]
    print(liste)
 #n= len(list_not_sorted)
    index = 0
    for j, i in zip(list_not_sorted, liste) :
    
        if j > i :
            liste.append(j)
        elif j <= i :
            liste.insert(index-1, j)
        print(liste[1:n])
        index +=1
        #return liste[1:n]


#print(sort_my_list(list_not_sorted))
sort_my_list(list_not_sorted)

# import random

# def sort_fonction (a,b,c):

#     liste_initiale = [random.randint(a,b) for i in range(c)]
#     liste_triée = []
#     print(liste_initiale)

#     for i in range(c):
#         valeur_min = min(liste_initiale)
#         liste_triée.append(valeur_min)
#         liste_initiale.remove(valeur_min)
#     return liste_triée

# print(sort_fonction(-1, 50, 40))