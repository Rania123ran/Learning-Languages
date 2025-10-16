#exercice1 :(périmètre et la surface d'un rectangle)
# longueur = eval(input("entrer la longueur du rectange : "))
# largeur = eval(input("entrer la largeur du rectange : "))
# P = (longueur+largeur)*2
# S = longueur*largeur
# print(f"le périmètre du rectange est :{P} \nla surface du rectange est:{S}")


# exercice2 :(la puissance x par y)
# print("la puissance x par y")
# x = int(input("entrer la valeur de x :"))
# y = int(input("entrer la valeur de y :"))
# methode 1 :
# p=1 
# for i in range(0,y):
#     p *=x
# print(f"la puissance de {x} par {y} est :{p}")
# methode 2 :
# print(f"la puissance de {x} par {y} est :",pow(x,y))



#exercice3 :(calculatrice)
# a = eval(input("entrer le premier nombre :"))
# b = eval(input("entrer le deuxiéme nombre :"))
# op = input("entrer l'operateur (+,-,/,*,^) :")
# if op == "+":
#     print(a,"+",b,"=",a+b)
# elif op == "-":
#     print(a,"-",b,"=",a-b)
# elif op == "/":
#     if b != 0 :
#         print(a,"/",b,"=",a/b)
#     else: 
#         print("devision impossible par 0")
# elif op =="*" :
#     print(a,"*",b,"=",a*b)
# elif op=="^" :
#     p = 1 
#     for i in range(0,b):
#         p *=a
#     print(a,"^",b,"=",p)
# else :
#     print("vous avez entrer un operateur incorrect")


#exercice3 :(la somme et la moyenne de 5 notes )
# n1 = eval(input("entrer la note1 :"))
# n2 = eval(input("entrer la note2 :"))
# n3= eval(input("entrer la note3 :"))
# n4= eval(input("entrer la note4 :"))
# n5 = eval(input("entrer la note5 :"))
# somme = n1 + n2 + n3 + n4 + n5 
# moyenne = somme /5
# print("la somme des notes est :",somme)
# print("la moyenne des notes est :",moyenne)


#ex 4 : (vollume de sphère:)
# from math import pi
# rayon = eval(input("entrer le rayon du sphère :"))
# volume = (4*pi*pow(rayon,3))/3
# print("le volume du sphére est :",volume)


#ex 5 :(echanger les variable )
#methode 1 : 
# a = int(input("entrer la valeur de a: "))
# b = int(input("entrer la valeur de b: "))
# a , b = b , a 
# print(f"a = {a} et b = {b}")
#methode 2: 
# a = int(input("entrer la valeur de a: "))
# b = int(input("entrer la valeur de b: "))
# c = a 
# a = b 
# b = c 
# print(f"a = {a} et b = {b}")


# ex 6 :(convertir une durée en h , min ,s )
# T = int(input("entrer une durée exprimé  en secondes : "))
# h = int(T/3600)
# R = T%3600
# min = int(R/60)
# s = R%60
# print(f"T ={T} =>{h} h {min} min {s} s")


#ex 7 :(comparaison de signe de deux nombre)
# a = int(input("entrer la valeur de a: "))
# b = int(input("entrer la valeur de b: "))
# if a*b > 0 :
#     print("a et b ils ont le même signe")
# else : 
#     print("a et b ils n'ont pas le même signe")


#ex 8 :
# a = int(input("entrer la valeur de a: "))
# b = int(input("entrer la valeur de b: "))
# if a*b > 0 :
#     a , b = b ,a 
# else : 
#     a, b = a+b , a*b
# print(f"a = {a} et b = {b}")


#ex 9 : (magasin de photocopie)
# n = int(input("entrer le nombre de photocopie :"))
# if n <= 10 :
#     F = n * 0.3
# elif n <=30 :
#     F = 10 *0.3 + (n-10)+0.25
# else  :
#     F = 10 *0.3 + 20*0.25 + (n-30)*0.2
# print("Facture :",F)


#ex 10 :
age = int(input("entrer l'age de votre enfant"))
if  6 <= age <= 7:
    print("poussin")
elif 8 <= age <= 9 :
    print("pupille")
elif 10 <= age <= 11 :
    print("minime")
elif age>=12 :
    print("cadet")














