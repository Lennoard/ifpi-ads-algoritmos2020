import java.util.Scanner;

public class q9 {

    public static void main(String[] args) {
        int start = readInt("Insira o limite inferior");
        int end = readInt("Insira o limite superior");

        if (end < start) for (int i = end; i < start; i++) {
            printEvenNumber(i);
        } else for (int i = start; i < end; i++) {
            printEvenNumber(i);
        }
    }

    private static int readInt(String message) {
        System.out.print(message + " ");
        return new Scanner(System.in).nextInt();
    }

    private static void printEvenNumber(int i) {
        if (i % 2 == 0) {
            System.out.println(i);
        }
    }

}
