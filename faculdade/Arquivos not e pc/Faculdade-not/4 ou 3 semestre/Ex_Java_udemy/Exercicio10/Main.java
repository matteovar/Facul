//Matteo Domiciano Varnier - 32158238
package Exercicio10;

import java.util.Scanner;

public class Main {
    public static void main(String[] args)  {
        
        Scanner s = new Scanner(System.in);

        System.out.print("\nX de p1: ");
        int x1 = s.nextInt();

        System.out.print("\nY de p1: ");
        int y1 = s.nextInt();

        System.out.print("\nRaio de p1: ");
        int r1 = s.nextInt();

        System.out.print("\nInsira o x de p2: ");
        int x2 = s.nextInt();

        System.out.print("\nY de p2: ");
        int y2 = s.nextInt();

        System.out.print("\nRaio de p2: ");
        int r2 = s.nextInt();

        boolean haColisao = Circulo.haColisaoEntreCirculos(x1, y1, r1, x2, y2, r2);
        System.out.println("\nOs os circlos estao:  " + haColisao);

        s.close();

    }
}
