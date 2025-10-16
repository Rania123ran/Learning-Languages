#ex 1 :
# l = int(input("saisir un nombre de lignes :"))
# for i in range(1,l+1):
#     for j in range(0,l-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()


#ex2 :(cadre étoile)
# l = int(input("entrer un nombre de ligne :"))
# c = int(input("entrer un nombre de colonne :"))
# for i in range(1,l+1):
#     for j in range(1,c+1):
#         if ( i == 1 or i == l):
#             print("*",end=" ")
#         elif ( j == 1 or j == c  ):
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")      
#     print()


#ex3 :(cadre etoile avec un motif au centre)
# l = int(input("entrer un nombre de ligne impaire:"))
# while l%2 ==0:
#     l = int(input("entrer un nombre de ligne IMPAIRE :"))
# for i in range(1,l+1):
#     for j in range(1,l+1):
#         if  (i == 1 or i == l):
#             print("*",end=" ")
#         elif (j == 1 or j == l):
#             print("*",end=" ")
#         elif  j == i :
#             print("*",end=" ")
#         elif j == l -i +1 :
#             print("*",end=" ") 
#         else : 
#             print(" ",end=" ")
#     print()


#ex 4 :(losange éroile)                  ##########################################
# l = int(input("entrer un nombre de ligne :"))
# for i in range(1,l+1):
#     for j in range(l-i):
#         print(" ",end=" ")
#     for k in range(1,l+1):
#         print("*",end=" ")
#     print()


#ex 5 :(triange  isocèle étoile )        ############################################
# l = int(input("entrer un nombre de ligne :"))
# for i in range(1,l+1):
#     for j in range(l-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()



#ex6 : (cadre triange étoile :)
# l = int(input("entrer un nombre de ligne :"))
# for i in range(1,l+1):
#     for j in range(l-i+1):
#         print(" ",end=" ")
#     for k in range(1,2*i-1+1):
#         if k == 1 or i == l or k == 2*i-1:
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()



#ex 7:(triangle isocéle etoile:)
# c = int(input("entrer un nombre de colonne :"))
# m = c-1
# for i in range(1,2*c):
#     if 1 <= i <= c :
#         for j in range(i):
#             print("*",end=" ")
#     elif c < i <= (2*c-1):
#         for k in range(1,m+1):
#             print("*",end=" ")
#         m= m-1
#     print()


#ex8 :(diamant d'etoile)
# l = int(input("entrer un nombre de ligne :"))
# m1 = l-1
# m2 = 1
# m3 = 0
# for i in range(1,2*l):
#     if 1 <= i <= l:
#         for j in range(1,m1+1):
#             print(" ",end=" ")
#         m1 = m1 - 1
#         for k in range(2*i-1+1):
#             print("*",end=" ")
#     else :
#         for m in range(1,m2+1):
#              print(" ",end=" ")
#         m2 = m2 + 1
#         for n in range(1,i-m3*3+1):
#              print("*",end=" ")
#         m3 = m3 + 1
#     print()



#ex9 :(table de multiplication )
# n = int(input("entrer un nombre entier positif :"))
# while n<0 :
#     n = int(input("entrer un nombre entier positif :"))
# print(f"Table de multiplication de {n} est :")
# for i in range(0,11):
#     print(n,"*",i,"=",n*i)


#ex10 :
# l = int(input("saisir le nombre de lignes :"))
# c = int(input("saisir le nombre de colonnes :"))
# n = 1
# for i in range(1,l+1):
#     for j in range(1,c+1):
#         print(n,end=" ")
#     n = n + 1
#     print()














    

    