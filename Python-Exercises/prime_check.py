number = int(input("enter a number  :"))
while number<1 : 
    print("only positif number greater  than 1 !")
    number = int(input("enter a number  :"))
cnt = 0 
for div in range(2,number):
    if number % div == 0 : 
        cnt += 1
if (cnt == 0): 
    print(number," est un numbre premier !")
else : 
    print(number," n'est pas un numbre premier !")