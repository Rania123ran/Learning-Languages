number1 = int(input("saisir le premier nombre :"))
number2 = int(input("saisir le deuxieme nombre :"))
l_number1 , l_number2 , l_comm = [] ,[] , []
for i in range(1,number1+1):
    if number1 % i == 0:
        l_number1.append(i)
for j in range(1,number2+1):
    if number2 % j == 0:
        l_number2.append(j)
for k in l_number1 : 
    if k in l_number2 : 
        l_comm.append(k)
for m in l_number2 : 
    if m in l_number1 : 
        l_comm.append(m)
if len(l_comm) != 0 :
    print("le grand diviseur commun est : ",max(l_comm))
else : 
    print("pas de diviseur commun !")



