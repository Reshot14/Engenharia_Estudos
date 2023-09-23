/**O programa deve cacular  a media das notas
nota 1 tem peso 30% 
nota 2 tem peso 50%
nota do trabalho tem peso 20% 
media minima para ser aprovado = 7 **/

#include <stdio.h>
int main(){
    float nota1;
    float nota2;
    float notatrabalho;
    float media;

    printf("Digite a nota 1: ");
    scanf("%f", &nota1);

    printf("Digite a nota 2: ");
    scanf("%f", &nota2);

    printf("Digite a nota do trabalho: ");
    scanf("%f", &notatrabalho);

    media = (nota1*0.3) + (nota2*0.5) + (notatrabalho*0.2);

    printf("\n Media = %0.2f\n\n", media);
    if(media < 7){
        printf("REPROVADO!\n");
    }else{
        printf("APROVADO!\n");
    }
}
