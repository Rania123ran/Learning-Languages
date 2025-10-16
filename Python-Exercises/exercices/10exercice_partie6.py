                                            
                                                        ################ FONCTIONS ########################


#ex1 :(tableau de multiplication)
# def multiple(k):
#     for i in range(1,11):
#         print(k,"*",i,"=",k*i)
# n = int(input("entrer un nombre entier positif :"))
# while n<0 :
#     n = int(input("entrer un nombre entier positif :"))
# multiple(n)


#ex2 :(cube d'un nombre)
# def cube(N):
#     print(f"le cube de {N} est:",pow(N,3))
# n = int(input("entrer un nombre réel :"))
# cube(n)
# cube(5)
# cube(7)


#ex3 : (nombre premier)
# def premier(N):
#     e = 0 
#     for i in range(2,N):
#         if N%i == 0 :
#             e = e+1
#     if e != 0 :
#         print("nombre n'est pas premier")
#     else :
#         print("nombre premier")
# n = int(input("entrer un nombre :"))
# premier(n)


#ex4 :(cercle)
# from math import pi
# def diametre (r):
#     return R * 2
# def perimetre(r):
#     return pi * r * 2
# def surface(r):
#     return pi * r * r
# R = eval(input("saisir un rayon de cercle :"))
# d = diametre(R)
# p = perimetre(R)
# s = surface(R)
# print("diamétre est:",d)
# print("perimetre est:",format(p,".2f"))
# print("surface est:",format(s,".2f"))


#ex 5 :(argumant par défaut)
# def affiche_employee(nom , salaire=3000):
#     print(f"nom :{nom}\nsalaire :{salaire} dh\n")
# affiche_employee("rania",100000)
# affiche_employee("ayoub",150000)
# affiche_employee("amal")


#ex6 :(equation)
# def equa(x):
#     return 4 * pow(x,3) - 13 * pow(x,2) + x - 60
# X = int(input("entrer une valeur :"))
# print("solution de l'equation 4*x^3 - 13*x^2 +x -60 est :",equa(X))


#ex7 :
# from math import sin , cos , pi 
# def f(x):
#     return cos(4*x)
# def f_prime(x):
#     return -4 * sin(4*x)
# def f_second(x):
#     return -16 * cos(4+x)
# print("f(x) = ",f(0),"f'(x) = ",f_prime(0),"f''(x) = ",f_second(0))
# print("f(x) = ",f(pi/2),"f'(x) = ",f_prime(pi/2),"f''(x) = ",f_second(pi/2))
# print("f(x) = ",f(pi),"f'(x) = ",f_prime(pi),"f''(x) = ",f_second(pi))
# print("f(x) = ",f(-pi/2),"f'(x) = ",f_prime(-pi/2),"f''(x) = ",f_second(-pi/2))

#ex8 :(validité d"un fonction)
# from math import cos , sin  
# def val(x,n=10):
#     s = 0
#     for i in range(0,n+1):
#         s = s + cos(i*x)
#     s1 = (1/2) + ((sin(((2*n+1)/2)*x))/(2*sin(x/2)))
#     print(format(s,".5f"))
#     print(format(s1,".5f"))
#     if s == s1 :
#         print("formule valide")
#     else :
#         print("la formule n'est pas valide")
# X = eval(input("saisir un chiffre :"))
# val(X)


#ex9 :(lancement d'un dé)
# from random import randint
# tour10 = 0
# tour1000 = 0
# for i in range(1,11):
#     robot = randint(1,6)
#     if robot == 2 or robot == 5 :
#         print("gagné",end="  ")
#         tour10 += 1
#     else : 
#         print("perdu",end="  ")
# print(f"\nvous avez gagner {tour10} fois en 10 jets de dés succesifs")
# for i in range(1,1001):
#     robot = randint(1,6)
#     if robot == 2 or robot == 5 :
#         tour1000 += 1
#     else : 
#         continue
# print(f"vous avez gagner {tour1000} fois en 100 jets de dés succesifs")



#ex10 :(suite syracuse )
# def syracuse(U0):
#     while U != 1 :
#         if U % 2 == 0 :
#             U = U//2
#             print(U,end=" ")
#         else :
#             U = 3*U + 1
#             print(U,end=" ")
# U0 = int(input("saisir une valeur :"))
# U = U0
# syracuse(U0)







    