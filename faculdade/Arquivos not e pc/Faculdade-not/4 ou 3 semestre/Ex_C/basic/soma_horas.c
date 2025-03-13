#include <stdio.h>
#include <stdlib.h>


 struct tempo{
    int horas;
    int minutos;
} ;

 struct tempo somahoras(struct tempo horario, int soma_minutos){
    int total = (horario.horas * 60)  + (horario.minutos) + soma_minutos;
    horario.horas = total /60;
    horario.minutos = total % 60;
    return horario;
}

int main(void){
   struct  tempo horario = {19, 30 };
    int soma_minutos = 30;
    printf("Horas inciais ficaram em %dhrs e %dmin", horario.horas, horario.minutos);

    horario = somahoras(horario, soma_minutos);

    printf("\nCom a adicao de %d, as horas atualizadas ficam em %dhrs e %dmin", soma_minutos, horario.horas, horario.minutos);

    return 0;
}
