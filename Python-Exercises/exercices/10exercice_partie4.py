#ex 1 :
# n = int(input("nombre d'equipe :"))
# print("LISTE DE MATCHS A DOMICILE :")
# for i in range(1,5):
#     for j in range(1,5):
#         if i == j :
#             continue
#         else :
#             print(f"equipe {i} vs equipe {j}")
#     print()


#ex2:
# import random
# n = random.randint(1,30)
# cnt = 1
# while cnt <= 5 :
#     m = int(input("entrer un nombre entre 1 et 30:"))
#     if m > n :
#         print("trop grand !")
#         cnt +=1 
#     elif m < n :
#         print("trop petit !")
#         cnt +=1 
#     elif m == n :
#         print(f"vous avez trouvez le Bon nombre  apres {cnt} tentatives ,BRAVO !!!")
#         break
#     if cnt > 5 :
#         print("vous avez atteint le nombre max de tentative")
        


#ex 3 :(calculatrice V2)
# while True :
#     print("calculatrice MENU :")
#     print("1- Addition\n2- Soustraction\n3- Multiplication\n4- Division\n5- Reste de la division\n6 -Puissance")
#     op = int(input("Quel calcule veux-tu effectuer ?"))
#     if op>= 0 and op>6:
#         print("vous avez entrer un nombre qui ne correspond pas au MENU")
#         print("resultats incorrect")
#         continue
#     a = eval(input("entrer le premier terme :"))
#     b = eval(input("entrer le deuxieme terme :"))
#     if op == 1 :
#         print(f"{a} + {b} = {a+b}")
#     elif op == 2:
#         print(f"{a} - {b} = {a-b}")
#     elif op == 3 :
#         print(f"{a} * {b} = {a*b}")
#     elif op == 4 :
#         if b != 0 :
#              print(f"{a} / {b} = ",format(a/b,".2f"))
#         else :
#             print("devision impossible par 0")
#     elif op == 5:
#         print(f"reste de devition de {a} / {b} est : {a%b}")
#     elif op == 6 :
#         print(f"{a} ^ {b} = {pow(a,b)}")
#     print("vous voulez demarrer une nouvelle operation oui/non")
#     rep = input()
#     if rep == 'non':
#         break
 

#ex 4 :(nombre de chiffre dans un entier)
# nbr = int(input("entrer un nombre entier :"))
# cnt = 0 
# while nbr != 0 :
#     m = nbr % 10
#     nbr = nbr // 10
#     cnt += 1
#     if m == 0 :
#         break
# print("nombre de chiffre est :",cnt)


#ex5 : (inverse d'un chiffre)
# n = int(input("entrer un nombre entier :"))
# nbr = 0
# while n != 0 :
#     m = n % 10
#     n = n // 10
#     nbr = nbr*10 + m
#     if m == 0 :
#         break
# print("l'inverse est :",nbr)


#ex 6 : (nombre palindrome)
# n = int(input("entrer un nombre entier :"))
# nbr1 = n
# nbr = 0
# while n != 0 :
#     m = n % 10
#     n = n // 10
#     nbr = nbr*10 + m
#     if m == 0 :
#         break
# if nbr1 == nbr :
#     print(nbr1,"est un nombre palindrome")
# else :
#     print(nbr1,"n'est pas un nombre palindrome")


#ex7 :(nombre parfait)
# n = int(input("entrer un  nombre entier :"))
# s = 0 
# for i in range(1,n):
#     if n%i ==0 :
#         s = s + i
# if s == n :
#     print(n,"nombre parfait")
# else :
#     print(n,"n'est pas un nombre parfait")


#ex 8 :(pierre , feuille , ciseaux)
# import random
# joueur = 0
# egalite = 0
# robot = 0 
# nom = input("entrer votre nom :")
# while True :
#     coup_j = input("choisir votre coup (pierre/feuille/ciseaux)  : ")
#     list1 = ["pierre","feuille","ciseaux"]
#     coup_pc = random.choice(list1)
#     if ((coup_j == "pierre") and (coup_pc =="ciseaux") or (coup_j == "ciseaux") and (coup_pc =="feuille") or (coup_j == "feuille") and (coup_pc =="pierre")) :
#         joueur += 1
#         print("vous avez gagner")
#         print("votre choix est :",coup_j,"et le choix du robot est :",coup_pc)
#         print("Score :",nom,":",joueur,"   ","robot :",robot,"   ","egalité : ",egalite)
#     elif ((coup_j == "pierre") and (coup_pc =="feuille") or (coup_j == "ciseaux") and (coup_pc =="pierre") or (coup_j == "feuille") and (coup_pc =="ciseaux")) :
#         robot += 1
#         print("vous avez échouer")
#         print("votre choix est :",coup_j,"et le choix du robot est :",coup_pc)
#         print("Score :",nom,":",joueur,"   ","robot :",robot,"   ","egalité : ",egalite)
#     elif coup_j == coup_pc :
#         egalite += 1
#         print("égalite")
#         print("Score :",nom,":",joueur,"   ","robot :",robot,"   ","egalité : ",egalite)
#     if (coup_j != "pierre" and coup_j != "feuille" and coup_j != "ciseaux") :
#         print("erreur de frappe")
#         continue
#     choice=int(input("vous voulez quitter le jeux taper 1 ou 0 '1: oui ou 0: non'  :"))
#     if choice == 1:
#         break
#     elif choice == 0 :
#         continue 
#     else :
#         while choice != 0 and choice !=1 :
#             choice=int(input("vous voulez quitter le jeux taper 1 ou 0 '1: oui ou 0: non'"))



#ex 9 : (décimal to binary)
# dec = int(input("entrer un nombre décimal :"))
# print("nombre décimal est : ",dec)
# inv_bin = 0
# while dec != 0 :
#     R = dec %2
#     dec = dec // 2
#     inv_bin = inv_bin *10 + R 
# #inverse du nombre binaire :
# bin = 0
# while inv_bin != 0 :
#     r = inv_bin % 10 
#     inv_bin = inv_bin // 10 
#     bin = bin*10 + r
# print("nombre binaire est :",bin)


#ex 10 :(triange étoile)
# l = int(input("entrer un nombre de ligne :"))
# for i in range(1,l+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()






    








    
