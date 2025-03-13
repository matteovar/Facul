//Matteo Domiciano Varnier - 32158238
package Exercicio1;

import java.util.Scanner;

public class inverter {
    public static void main(String[] args){
        Scanner s =new Scanner(System.in);

        System.out.print("Primeiro valor: ");
        int valor1 = s.nextInt();

        System.out.print("Segundo valor: ");
        int valor2 = s.nextInt();

        System.out.printf("Valores digitados foram: Valor1 = %d e Valor2 = %d\n",valor1, valor2);

        int aux = valor1;
        valor1 = valor2;
        valor2 = aux;

        System.out.printf("Os valores invertidos sao: Valor1 = %d e Valor2 = %d",valor1, valor2);
        s.close();
    }



}
