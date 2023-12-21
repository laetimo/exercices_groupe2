
def serie_impair(a,b):
    ma_liste = []

    for i in range (int(a),int(b)+1):
        if i % 2 > 0 :
            ma_liste.append(i)
    

    ma_liste = str(ma_liste).replace(",","") \
            .replace("[","").replace("]","")
    return ma_liste

print(serie_impair(42.75,53.23))