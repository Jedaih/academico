#include <stdio.h>
int main(void)
{
    int contador;
    printf("\nDigite um numero para a contagem regressiva: \n\n");
    scanf("%d", &contador);
        for(contador; contador >= 1; contador--)
        {
            printf("%d", contador);
        }
    getch();
    return(0);


}