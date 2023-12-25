# import random as rn
# list_initiale = [rn.randint(1,100) for i in range(100)]
# list_extract = []
# print('list_initiale', list_initiale)
# for i in list_initiale:
#     if i[0] == max(list_initiale ) :
#         list_extract.append()


# while len(list_extract) < 10 :
#  for i in list_initiale :

 
#    if i[0] > i[1] :
#       list_extract.append()
# print(list_extract)

  
#
import random as rn 
#list = []
list = [8,6,9,5,7,1,2]


list_new= []          
#list_not_sorted = [rn.randint(5,20) for i in range (10)]
#print(list_not_sorted)
#n = len(list)

def sort_my_list(list) :
#n = len(list)
 
 for i in list :
        
       if i == min(list) :
        list_new.append(i)
        return i
    
list = [8,6,9,5,7,1,2]
print(list_new)
sort_my_list(list)
print(sort_my_list(list))


# list1 = [2,5,9,8,7,4,2,1] 
# a = sort_my_list(list1)
# print (a) 
#       # #for j in list_not_sorted :
#       #    if j[i] > j[i+1] :
#       #       j[i],j[i+1] =  j[i+1],j[i]
#       #       return
             
# # print(sort_my_list())             

# list = [2,55,1,5,8,6]
# sort_my_list(list)
# print(sort_my_list(list))






