//Felipe Mazzeo Barbosa - 32257023
//Matteo Domiciano Varnier - 32158238

public class Palindromo {
    private String textoInvertido = "";
    private String texto = "";

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public boolean verificaPalindromo() {
        for (int i = texto.length() - 1; i >= 0; i--) {
            textoInvertido += texto.charAt(i);
        }
        return texto.equals(textoInvertido);
    }
}

//Referencias:

//https://www.youtube.com/watch?v=kd3dr39rgrk
//https://www.youtube.com/watch?v=lhf8gaUx4yU
//https://javawithumer.com/2018/09/getters-and-setters-lesson-28.html7
//https://www.w3schools.com/java/java_encapsulation.asp
//https://docs.oracle.com/javase/tutorial/java/data/manipstrings.html
//https://www.sanfoundry.com/java-program-check-whether-string-palindrome/