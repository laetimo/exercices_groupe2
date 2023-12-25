# dict_fr_en = {"mot1":"mot_1","mot2":"mot_2","mot3":"mot_3"}
# dic_en_fr = dict_fr_en.fromkeys()
# print(dic_en_fr)
# dic1 = {}
# a=list(dic1.keys())
# b = list(dic1.values())
# fr_color = ["rouge" ,"blue","vert","jaune","noir","blanc" ]
# en_color = ["red","blue","green","yello","black","white"]
# dict_fr_en = dict(fr_color,en_color)
key = []
value = []
dict_1 = dict(zip(key,value))

def revers_key_value (dict_1):
#  for key,value in dict_1 :
#  dict_1 = dict(zip(key,value))
    dict_2 = dict(zip(value,key))
    print(dict_2)

key  = ["rouge" ,"blue","vert","jaune","noir","blanc" ]
value = ["red","blue","green","yello","black","white"]
dict_fr_en = dict(zip(key,value))  
y = revers_key_value(dict_fr_en)
print(y)    