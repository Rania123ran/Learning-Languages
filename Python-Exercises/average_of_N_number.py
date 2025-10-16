number = int(input("veuillez saisir le nombre de numéro : "))
sum = 0 
for i in range(number):
    num = float(input("Saisir un nombre :"))
    sum += num 
print("la moyenne est : ",sum/number)