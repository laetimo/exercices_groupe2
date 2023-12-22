# Écrire un programme qui convertit un nombre entier de secondes fourni au départ, en un
# nombre d'années, de mois, de jours, de minutes et de secondes.
# Contraintes:
# • Ne pas utiliser le package datetime
# • Afficher le résultat sous la forme :
# 3430061596791935255 secondes correspondent à :
# 108 692 093 086 années 8 mois 1 jours
# 15 heures 51 minutes 28 secondes

def convert_date(nb_secondes):
    nb_minutes = nb_secondes // 60
    reste_secondes = nb_secondes % 60

    nb_heures = nb_minutes // 60
    reste_minutes = nb_minutes % 60

    nb_jours = nb_heures // 24
    reste_heures = nb_heures % 24

    nb_annees = nb_jours // 365.25
    reste_jours = nb_jours % 365.25
    reste_heures = reste_heures + (reste_jours - int(reste_jours))*24
    if reste_heures >= 24 :
        reste_heures = reste_heures - 24
        reste_jours = reste_jours + 1 
    
    nb_mois = int(245/365.25*12)
    reste_jours2 = int(reste_jours) - nb_mois/12*365.25
    #print(nb_mois, " mois et ", reste_jours2, " jours")

    reste_heures2 = reste_heures + (reste_jours2 - int(reste_jours2))*24

    print(f" {int(nb_annees)} années {int(reste_jours)} jours {int(reste_heures2)} heures {reste_minutes} minutes {reste_secondes} secondes")
    print(f" {int(nb_annees)} années {nb_mois} mois {int(reste_jours2)} jours {int(reste_heures2)} heures {reste_minutes} minutes {reste_secondes} secondes")


convert_date(3430061596791935255)

def convertion_vitesse (miles_heures):

    metres_heures = miles_heures / 0.00062137
    print(f"{metres_heures}m/h")

    metres_secondes = round (metres_heures/3600, 2)
    km_heures = round (metres_heures/1000, 2)

    return print(f"Pour {miles_heures} miles/heures, on a {metres_secondes} m/s et {km_heures} km/h")

convertion_vitesse(10)
