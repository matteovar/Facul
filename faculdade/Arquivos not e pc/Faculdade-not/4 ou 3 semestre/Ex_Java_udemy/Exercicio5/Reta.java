//Matteo Domiciano Varnier - 32158238
package Exercicio5;

import java.util.Scanner;

public class Reta {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        System.out.print("Digite um valor para X: ");
        int x = s.nextInt();

        System.out.print("Digite um valor para Y: ");
        int y = s.nextInt();

        int resultado = 3*x + y;

        if(resultado == 8){
            System.out.printf("Os pontos pertencem a reta");
        }else {
            System.out.printf("Os pontos nao pertencem a reta");
        }

        s.close();
    }
    
}
