#include <stdio.h>

int main(){
    int n;
    float media = 0;

    printf("digite a quantidade de notas: ");
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        printf("Digite a nota %d: ",(i+1));
        float nota;
        scanf("%f", &nota);
        media = media + nota;


    }
    media = media/n;


    printf("\nA media é: %0.2f\n", media);
}