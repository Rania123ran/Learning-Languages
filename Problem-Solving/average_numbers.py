total_nombres = int(input("How many numbers ?"))
sum = 0
for i in range(total_nombres) : 
    number= int(input("Enter a number :"))
    sum += number
average = sum / total_nombres
print("Average :",average)