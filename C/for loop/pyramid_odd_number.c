#include <stdio.h>
#include <stdlib.h>
/* *
  * *
 * * *
* * * *
*/
int main(){
int n , new_n = 1 ;
printf("entrer le nombre de ligne :");
scanf("%d",&n);
for(int i = 1 ; i<=n ; i++){
    for(int j = 1 ; j<=n-i ;j++){
        printf(" ");
    }
    for(int k=1 ; k<= new_n; k++){
        printf("*");
    }
    new_n += 2 ;
    printf("\n");
}
}
