#include <stdio.h>
#include <stdlib.h>
int main(){
/*
The pattern like :
*
**
***
****
*/
int n ;
printf("entrer le nombre de ligne :");
scanf("%d",&n);
for(int i=1;i<=n;i++){
    for(int j= 1;j<=i;j++){
        printf("*");
    }
    printf("\n");

}


}

