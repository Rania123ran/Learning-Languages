#ex1 :(moyenne et mention)
# n1 = eval(input("entrer la note 1 :"))
# n2 = eval(input("entrer la note 2 :"))
# n3 = eval(input("entrer la note 3 :"))
# m = (n1+n2+n3)/3
# print("votre moyenne est :",format(m,".2f"))
# if m >= 16 :
#     print("mention : Trés bien")
# elif 14<= m <= 16 :
#     print("mention : Bien")
# elif 12 <= m <= 14 :
#     print("mention : Assez bien")
# elif 10 <= m <= 12 :
#     print("mention : passable")
# else :
#     print("insuffisant")


#ex2 :(solution d'equatuion de second degrés):
# from math import sqrt
# print("equation second degrés ax^2 + bx + c")
# a = int(input("entrer la valeur de a : "))
# b = int(input("entrer la valeur de b : "))
# c = int(input("entrer la valeur de c : "))
# delta = pow(b,2) - 4*a*c
# if delta>0 :
#     x1 = (-b -sqrt(delta))/(2*a)
#     x2 = (-b +sqrt(delta))/(2*a)
#     print(f"les solutions de {a}x^2 + {b}x + {c} sont : {x1} et {x2}")
# elif delta<0:
#     x = -b / 2*a
#     print(f" solution de {a}x^2 + {b}x + {c} est : {x}")
# else : 
#     print(f"pas de solutions pour l'equatuion {a}x^2 + {b}x + {c}")


#ex3 :(impot pour une ville)
# age = int(input("entrer votre age:"))
# sexe = input("entrer votre sexe F/FEMME ou H/HOMME :")
# if (sexe == "HOMME" or sexe =="H") and age > 20 :
#     print("imposable")
# elif (sexe == "FEMME" or sexe =="F") and 18 <=age <=35:
#     print("imposable")
# else :
#     print("non imposable")


#ex 4 :( prix TTC d'un produit)
# Prix = eval(input("entrer le prix hors tax :"))
# c = input("entrer sa catégorie :")
# if c =="A" or c =="a":
#     ttc = Prix + Prix*0.07
# elif c =="B" or c =="b":
#     ttc = Prix + Prix*0.2
# elif c =="C" or c =="c":
#     ttc = Prix + Prix*0.25
# print("le prix ttc  est : ",ttc)


#ex 5 :(boucle for / while)
# a = int(input("entrer le nombre de départ"))
# for i in range(a+1,a+11):
#     print(i)
# a = int(input("entrer le nombre de départ"))
# i = a 
# while i < a+10 :
#     i += 1
#     print(i)


#ex 6 :(somme d'une serie harmonique s = 1/1 +1/2 + ....+1/n)
# n=int(input("entrer le nombre n  :"))
# s = 0
# for i in range(1,n+1):
#     s +=(1/i)
# print("somme d'une serie harmonique s = 1/1 +1/2 + ....+1/",n," est :" ,format(s,".2f"))


#ex7 :(somme d'une serie s = 1+10+100+......+10^n)
# n=int(input("entrer le nombre n  :"))
# s =  0
# for i in range(0,n+1) :
#     s = s + pow(10,i)
# print(f"somme  d'une serie s = 1+10+100+......+10^{n} est {s}")


#ex8 : (factorielle)
# a = int(input("entrer un nombre positif non nul :"))
# while a<=0 :
#     a = int(input("entrer un nombre positif non nul :"))
# p = 1 
# for i in range(1,a+1):
#     p = p * i
# print(f"le factorielle de {p} est : {p}")


#ex 9 :(la somme des carrées des n premiers entiers impairs)
# a = int(input("entrer un nombre  :"))
# i = 0
# j = 1
# s = 0
# while i < a :
#     s = s + pow((i+j),2)
#     i += 1
#     j += 1
# print("la somme est :",s)


#ex 10 :
# n = int(input("entrer l'age de amal :"))
# s = 0
# for i in range(1,n+1):
#     s = s + 500+i*3
# print(f"la somme qui aura amal lors de {n}ieme anniversaire est : {s}")










