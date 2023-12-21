import random

compteur_final = 0
play_again = "oui"

while play_again == "oui":

    print("1 - niveau facile")
    print("2 - niveau difficile")
    debut_plage = 1
    fin_plage = 100

    niveau_choisi = int(input("sélectionnne ton niveau : "))
    if niveau_choisi == 1 :
        debut_plage = 1
        fin_plage = 100
    elif niveau_choisi == 2 :
        debut_plage = 1
        fin_plage = 500
    else :
        print("du coup, ça sera facile")

    nb_a_trouver = random.randint(debut_plage,fin_plage)

    print(nb_a_trouver)

    nb_utilisateur = 0
    compteur = 0

    while nb_utilisateur != nb_a_trouver :
        nb_utilisateur = int(input(f"donner un nombre entre {debut_plage} et {fin_plage} : "))
        if (nb_utilisateur < debut_plage or nb_utilisateur > fin_plage) :
            print("ERREUR, le nombre n'est pas dans la plage")
        
        elif nb_utilisateur < nb_a_trouver :
            print("le chiffre donné est trop petit")
        elif nb_utilisateur > nb_a_trouver :
            print("le chiffre donné est trop grand")
        compteur += 1
        print("")

    print(f"vous avez trouvé le nombre en {compteur} coups !")
    compteur_final += compteur
    play_again = input("voulez-vous rejouer ? ")
    

print(f"merci d'avoir joué ! vous avez réalisé vos parties en {compteur_final} coups !")
