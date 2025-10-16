num = int(input("saisir un nombre positif :"))
while (num<0):
    num = int(input("saisir un nombre positif ! :"))
if (num == 0):
    fact = 1
else :
    fact = 1 
    for i in range(1,num+1):
         fact *= i 
print("Factorial de ",num," est :",fact)
 
    