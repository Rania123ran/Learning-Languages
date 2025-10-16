#ex 1 :
# pop_kech =1000000
# pop_agadir =500000
# nbr_annee = 0
# while pop_kech > pop_agadir:
#     pop_kech=pop_kech + 50000
#     pop_agadir = pop_agadir + pop_agadir*0.08
#     nbr_annee += 1
# print("agadir depaserra kech dans:",nbr_annee)

#ex2 :( U0= 6 et Un+1= 4Un + 10)
# n = int(input("entrer un rang :"))
# l = 6
# for i in range(1,n+1):
#     m = 4*l +10 
#     l = m 
# print("Un =",l)


#ex3 :(suite fibonacci)
# n = int(input("taper un nombre supérieur à 2 :"))
# while n <= 2 :
#     n = int(input("taper un nombre supérieur à 2  :"))
# a = 0 
# b = 1 
# print("les termes de la suites fibonacci sont :")
# print(a)
# print(b)
# for i in range(2,n+1):
#     u = b + a 
#     a = b 
#     b = u 
#     print(b)


#ex4 :(distance entre deux point)
# from math import sqrt
# print("entrer les coordonnées du point A")
# Xa = eval(input("Xa ="))
# Ya = eval(input("Ya ="))
# print("entrer les coordonnées du point B")
# Xb = eval(input("Xb ="))
# Yb = eval(input("Yb ="))
# AB = sqrt(pow(Xa-Xb,2)+pow(Yb-Ya,2))
# print("distance entre A et B est:",AB)


#ex 5 :(programme resistance)
# R1 = eval(input("entrer la valeur de R1 = "))
# R2 = eval(input("entrer la valeur de R2 = "))
# R3 = eval(input("entrer la valeur de R3 = "))
# print("en serie :")
# Rser = R1 +R2 +R3
# print("Rser =",format(Rser,".2f"))
# print("en parallèle : ")
# Rpar= (R3*R2*R1)/(R1*R2+R2*R3+R3*R1)
# print("Rpar  =",format(Rpar,".2f"))


#ex 6 :(nombre pair ou impair)
# n = int(input("entrer un nombre :"))
# if n%2 == 0 :
#     print("nombre pair")
# else :
#     print("npmbre impair")


#ex 7 :(verifier c'est l'année est bissextile):
# year = int(input("entrer une année :"))
# if year % 4 ==0 and year % 100 != 0 :
#     print(f"l'année {year} est bissextile")
# else : 
#     print(f"l'année {year} est normale")


#ex8 : (verifecation d'un nombre)
# nbr = input("entrer un nombre :")
# if 'a'<= nbr <= "z"  or "A" <= nbr <= "Z":
#     print("caractère donné est un alphabet")
# elif "0"<= nbr <="9" :
#     print("caractère donné est un nombre")
# else : 
#     print("caractère donné est un caractère special")


#ex9 : (diviseur)
# n = int(input("entrer un nombre positif non nul :"))
# while n <= 0 :
#     n = int(input("entrer un nombre positif non nul :"))
# print(f"les diviseur de {n} sont:")
# for i in range(1,n+1):
#     if n % i == 0 :
#         print(i)


#ex10 : (nombre premier)
# n = int(input("entrer un nombre :"))
# m = 1
# for i in range(2,n):
#     if n%i ==0 :
#         m += 1
#         break 
# if m == 1 :
#     print("nombre premier")
# else : 
#     print("nombre non premier")