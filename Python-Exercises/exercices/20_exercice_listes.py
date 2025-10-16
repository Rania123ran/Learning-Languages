#ex1 :
# lst  = list(range(5,15))
# print("premier liste :")
# print(lst)
# for i in range(0,10):
#     lst[i]=0
# print("deuxième liste")
# print(lst)

#ex2 : declarer une liste avec des 0 :
# lst = [0]*10 
# print(lst)

#ex3 :
# lst = list('aeiouy')
# print(lst)

#ex4 :
# lst = []
# print("saisir 10 réel:")
# for i in range(5):
#     print("valeur ",i+1,":",end="")
#     lst.append(float(input()))
# print(lst)
# sm = sum(lst)
# prd = 1
# for i in lst :
#     prd = prd*i
# myn = sm / len(lst)
# print("somme :",sm)
# print("produit :",prd)
# print("moyenne :",myn)

#ex5 :produit scalaire + 2 dimension (zip permet de parcourir deux liste au même temps)
#solution 1 :
# v = []
# u = []
# print("vecteur 1 :")
# for i in range(3):
#     v.append(int(input(f"valeur {i+1} :")))
# print("vecteur 2 :")
# for i in range(3):
#     u.append(int(input(f"valeur {i+1} :")))
# s = 0
# for i in range(3):
#     s = s + u[i]*v[i]
# print("produit scalaire de deux vecteurs est :",s)
#solution 2 :
# v = []
# u = []
# for i in range(3):
#     print(f"V[{i+1}]=",end="")
#     v.append(float(input()))
#     print(f"U[{i+1}]=",end="")
#     u.append(float(input()))
# s = 0 
# for ve ,ue in zip(v,u):
#     s = s + ve*ue
# print("produit scalaire de deux vecteurs est :",s)


#ex6 : afficher les élements unique dans une list :
# lst = []
# lst2 =[]
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# print(lst)
# for n in lst :
#     cnt = lst.count(n)
#     if cnt == 1 :
#         lst2.append(n)
#     else :
#         continue
# print(lst2)

#ex7 :(max et min d'une liste)
# lst = list(())
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# max = max(lst)
# min = min(lst)
# print(f"max est :{max} et min est :{min}")

#ex8 :
#solution 1 :
# lst = list(())
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# lst2=sorted(lst)
# print(lst2[len(lst)-2])

#ex9 :
# lst = list(())
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# lst2 = []
# for n in lst :
#     if n % 2 == 0 :
#         lst2.append(n)
#     else :
#         continue
# print(lst2)

#ex10 :
#solution 1 :
# lst = list(())
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# n = int(input("entrer un nombre entier"))
# for i in lst :
#     cnt = 0 
#     if n == i :
#         cnt = cnt +1 
#         break
#     else : 
#         continue
# if cnt != 0 :
#     print(n,"existe dans la list.")
# else :
#     print(n,"n'existe pas dans la list.")
#solution 2 :
# lst = list(())
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# n = int(input("entrer un nombre entier"))
# if n in lst :
#     print(n,"existe dans la list.")
# if n not in lst :
#     print(n,"n'existe pas dans la list.")

#ex11 :
# lst = list(())
# for i in range(10):
#     lst.append(int(input(f"valeur {i+1}:")))
# n = int(input("entrer un nombre entier:"))
# cnt = lst.count(n)
# print(f"nombre d'occurence de {n} dans la liste est :{cnt}")

#ex12 :notes de classe
# lst =  []
# for i in range(10):
#     lst.append(float(input(f"valeur {i+1}:")))
# s = sum(lst)
# my = s / len(lst)
# lst2 = []
# for n in lst :
#     if n > my : 
#         lst2.append(n)
#     else : 
#         continue
# print("moyenne de classe est :",format(my,".2f"))
# print("nombre de notes supérieure à la moyenne est :",len(lst2))

#ex13 :
# somme = 1000
# lst = []
# for i in range(20):
#     somme = somme + somme*0.02
#     lst.append(format(somme,".2f"))
# for i , j in enumerate(lst,start=1):
#     print(f"année {i} : {j}")

#ex14:inverser une liste
# lst = [1,2,3,4,5,6]
# lst2 = []
# for i in range(5,-1,-1):
#     lst2.append(lst[i])
# print(lst)
# print(lst2)

#ex15 :comparer deux list
# lst1 = []
# lst2 = []
# print("remplir la première list:")
# for i in range(6):
#     lst1.append(eval(input(f"valeur {i+1}:")))
# print("remplir la deuxième list:")
# for i in range(6):
#     lst2.append(eval(input(f"valeur {i+1}:")))
# cnt = 0
# for i in lst1:
#     for j in lst2 :
#         if i==j:
#             cnt = cnt +1
#         else :
#             continue
# if cnt != 0 :
#     print("les deux listes ont au moins un élement en commun")
# else : 
#     print("les deux listes n'ont pas d'élement commun")

#ex16 :
# phrase = input("entrer une phrase :")
# lst = list(phrase)
# lettre = input("entrer une lettre :")
# cnt = 0 
# for i in lst :
#     if i == lettre : 
#         cnt = cnt + 1 
#     else : 
#         continue 
# print(f"nombre d'occurence de la lettre '{lettre}' est : {cnt}")

#ex17 :
# def f1():
#     n = int(input("entrer la valeur de n :"))
#     print("entrer les éléments de la liste :")
#     lst = []
#     for i in range(n):
#         lst.append(int(input(f"valeur {i+1} :")))
#     return n , lst
# def f2(n,lst):
#     m = int(input("entrer la valeur de m :"))
#     while(m>n):
#         m = int(input("entrer la valeur de m :"))
#     lst.sort()
#     return lst[-m:]
# n,lst = f1()
# lst2 = f2(n,lst)
# print(lst)
# print(lst2)

#ex18 :
# def f1():
#     n = int(input("entrer la valeur de n :"))
#     print("entrer les éléments de la liste :")
#     lst = []
#     for i in range(n):
#         lst.append(int(input(f"valeur {i+1} :")))
#     return lst
# def f2(lst): 
#     for i in list(lst) :
#         if i % 5 == 0 : 
#             lst.remove(i)
#         else :
#             continue 
#     return lst
# lst = f1()
# lst = f2(lst)
# print(lst)

#ex19 : 
# n = int(input("entrer un nombre n :"))
# while (n<2):
#     n = int(input("entrer un nombre n (n>2) :"))
# lst = []
# for i in range(n):
#     lst.append(int(input(f"list[{i+1}]=")))
# lst1 = list(lst)
# for i in range(n-2):
#     lst1[i]=lst[i+1]+lst[i+2]
# print(lst)
# for i in range(-2,0):
#     if i == -2 :
#         lst1[i] = lst[-1] + lst[0]
#     if i == -1 :
#         lst1[i] = lst[0] + lst[1]
# print(lst1)

#ex20 :
#solution1 :
# lst = []
# for i in range(10):
#     lst.append(int(input(f"list[{i+1}]=")))
# list1 = sorted(lst)
# print(list1)
#solution 2 :
lst = []
for i in range(10):
    lst.append(int(input(f"list[{i+1}]=")))
def deplacer():
    lst1 = []
    min = lst[0]
    for i in lst:
        if i < min :
            lst1.append(i)
            min = i 
        else : 
            continue
    return lst1
ls = deplacer()
print(ls)









     
