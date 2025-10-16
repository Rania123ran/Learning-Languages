#include <stdio.h>
#include <stdlib.h>
/* 1
  2 2
 3 3 3
4 4 4 4
*/
int main(){
int n , m= 1 ;
printf("entrer le nombre de ligne :");
scanf("%d",&n);
for(int i = 1 ; i<=n ; i++){
    for(int j = 1 ; j<=n-i ;j++){
        printf(" ");
    }
    for(int k=1 ; k<=i; k++){
        printf("%d ",m);
    }
    m++ ;
    printf("\n");
}

}
