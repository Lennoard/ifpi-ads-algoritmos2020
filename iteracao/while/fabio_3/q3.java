import java.util.Scanner;

public class q3 {

    public static void main(String[] args) {
        int start = readInt("Insira o A₀");
        int end = readInt("Insira o limite");
        int r = readInt("Insira a razão");

        if (end < start) throw new IllegalArgumentException("Limite menor que A₀");

        for (int i = start; i <= end; i += r) {
            System.out.println(i);
        }
    }

    static int readInt(String message) {
        System.out.print(message + " ");
        return new Scanner(System.in).nextInt();
    }
}
