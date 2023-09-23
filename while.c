/*FACA UM PROGRAMA QUE DADO UMA LITA DE NUMEROS FORNECE O MAIOR DELES*/

#include <stdio.h>
int main(){
    int n;
    int maior=0;
    printf("Digite a quantidade de numeros que deseja inserir: ");
    scanf("%d", &n);

    for(int i=0;i<n;i++){
        printf("Digite o numero %d: ", (i+1));
        
        int numeros;
    scanf("%d", &numeros);
    if(i==1 || numeros>maior){
        maior=numeros;
    }

    }
    printf("\nO maior numero é: %d\n", maior);
    return 0;
}