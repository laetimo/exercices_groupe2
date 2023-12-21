import random
play_again = "oui"
compteur_final = 0

while play_again == "oui":

    print("niveau 1: tapez 1")
    print("niveau 2: tapez 2")
    niveau_de_difficulté = 0

    while niveau_de_difficulté != 1 or niveau_de_difficulté != 2:
        niveau_de_difficulté = int(input("sélectionner le niveau de difficulté: "))
        if niveau_de_difficulté == 1:
            debut_plage = 1
            fin_de_plage = 100
            break
            
        elif niveau_de_difficulté == 2:
            debut_plage = 1
            fin_de_plage = 200
            break

    chiffre_a_trouver = random.randint(debut_plage, fin_de_plage)
    print(chiffre_a_trouver)
    chiffre_donné = 0
    compteur = 0 

    while chiffre_donné != chiffre_a_trouver:
        chiffre_donné = int(input(f"Trouvez le chiffre entre {debut_plage} et {fin_de_plage}: "))
        if chiffre_donné < debut_plage  or chiffre_donné > fin_de_plage:
            print("Rester dans la plage donné")
        elif chiffre_donné < chiffre_a_trouver:
            print("le chiffre est trop petit, réessayez")
        elif chiffre_donné > chiffre_a_trouver:
            print("le chiffre est trop grand, réessayez")
        compteur += 1
        print("")

    print(f"vous avez gagné en {compteur} coups :)")
    compteur_final += compteur
    play_again = input("voulez-vous rejouer ? Tapez oui ou non ")

print(f"Vous avez réalisé un total de {compteur_final} coups ! Bravo")
    
        



