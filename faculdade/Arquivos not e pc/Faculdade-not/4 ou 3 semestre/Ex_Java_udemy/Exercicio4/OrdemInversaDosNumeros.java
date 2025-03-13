//Matteo Domiciano Varnier - 32158238
package Exercicio4;

import java.util.Scanner;

public class OrdemInversaDosNumeros {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        int[] numeros = new int[10];

        for(int i =0; i< 10;i++ ){
            System.out.print("Digite o "+(i+1)+"º numeros: ");
            numeros[i] = s.nextInt();
        }
        
        for (int i = 9; i>=0;i--){
            System.out.print("Na ordem inversa fica:"+numeros[i]+"-" );
        }
        s.close();
    }

}
