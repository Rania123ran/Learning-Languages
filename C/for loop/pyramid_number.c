#include <stdio.h>
#include <stdlib.h>
/*
   1
  2 3
 4 5 6
7 8 9 10
*/
int main(){
int n, k = 1 ;
printf("entrer le nombre de ligne :");
scanf("%d",&n);
for(int i=1;i<=n;i++){
    for(int j=1;j<=n-i;j++){
        printf(" ");
    }
    for(int m=1;m<=i;m++){
        printf("%d ",k++);
    }
    printf("\n");
    }}
