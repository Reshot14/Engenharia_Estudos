#include <stdio.h>
int main(){
    float n;
    float z;
    float div;
    int contador_de_divs_sr=0;
    int contador_de_primos=0;
    printf("n: ");
    scanf("%f", &n);
    z = n-1;

    while(n>1){
        for(z; z>1; z--)
        {
        div = n/z;
       //printf("\n%f\n", div);
        int inteiro1 = (int)z;
        int inteiro2 = (int)n;
        int resto = inteiro2 % inteiro1; 
        if(resto==0){
            contador_de_divs_sr++;
            break;}
        if(contador_de_divs_sr==0){
        contador_de_primos++;}}
        
    if(n>1){n--;}
    printf("\n%f\n", n);}
    printf("\n%d\n", contador_de_primos);
}