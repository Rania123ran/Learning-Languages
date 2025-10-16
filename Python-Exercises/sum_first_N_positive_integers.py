sum = 0
num = int(input("Vueillez saisir un nombre :"))
while num<0:
    num = int(input("Vueillez saisir un nombre supérieure à 0 :"))
for i in range(1,num+1):
    sum += i 
print("la somme des premier ",num,"entier est : ",sum)