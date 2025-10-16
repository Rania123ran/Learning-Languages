number = int(input("Saisir un nombre : "))
sum = 0
if number <1 : 
    number = int(input("Saisir un nombre positif : "))
list_factors = []
for i in range(1,number+1):
    if number%i == 0 :
        list_factors.append(i)
if len(list_factors)!=0 :
    for i in list_factors :
        sum += i
    if sum == 2*number :
        print(number," est un nombre parfait !")
    else : 
        print(number,"n'est un nombre parfait !")



    

