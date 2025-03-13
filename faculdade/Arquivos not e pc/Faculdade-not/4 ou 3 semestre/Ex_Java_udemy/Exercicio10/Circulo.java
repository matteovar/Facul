//Matteo Domiciano Varnier - 32158238
package Exercicio10;

public class Circulo {
    public static boolean haColisaoEntreCirculos(int x1, int y1, int r1, int x2, int y2, int r2) {
        double distancia = Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
        
        if (distancia <= (r1 + r2)) return true;
            return false;
        
    }
}
