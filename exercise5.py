# from numpy import *

number = 3430061596791935255
def converti_temps(number) :
 
  to_year = 60*60*24*365.25
  n_year = int(number//to_year)
  #print(n_year)
  rest_1 = number % n_year
#print(rest_1)
  n_month = int(rest_1//(60*60*24*30.43))
  #print(n_month)
  rest_2 = rest_1 % (60*60*24*30.43)


                    # datetime64:

  n_day = int(rest_2//(60*60*24*12))






  #print(n_day)
  rest_3 = rest_2 % (60*60*24*12)
#print(rest_3)
  n_hour = int(rest_3 // (60*60*24))
  #print(n_hour)
  rest_4 = rest_3 % (60*60*24)





  n_min = int(rest_4//(60*60))
  #print(n_min)
  rest_5 = rest_4 % 60
  n_sec = rest_5
  #print(n_sec)
              


                    

