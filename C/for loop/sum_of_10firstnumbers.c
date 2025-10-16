/*Write a C program to compute the sum of the first 10 natural numbers.
Expected Output :
The first 10 natural number is :
1 2 3 4 5 6 7 8 9 10
The Sum is : 55*/
#include <stdio.h>
#include <stdlib.h>
int main (){
//printf("The first 10 natural number is :");
//int s = 0 ;
//for(int i=1;i<=10;i++){
//    printf("%d ",i);
//    s += i ;}
//printf("\nThe Sum is : %d",s);
//---------------------------------------------------------------
//Input the 10 numbers :
//Number-1 :2
//...
//Number-10 :2
//Expected Output :
//The sum of 10 no is : 55
//The Average is : 5.500000
   int s = 0 ;
   float avg ;
   int n ;
for(int i=1;i<=10;i++){
        printf("Number-%d : ",i);
        scanf("%d",&n);
        s += n ;
}
avg = s / 10. ;
printf("\nThe sum of 10 no is :%d",s);
printf("\nThe Average is :%.2f",avg);
}

