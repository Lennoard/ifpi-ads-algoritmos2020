import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class q12 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Insira a quantidade de números da lista ");
        int n = scanner.nextInt();

        System.out.println("Insira os números");
        List<Double> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(scanner.nextDouble());
        }

        double sum = 0;
        for (Double i : list) sum += i;

        double average = sum / list.size();

        System.out.println("Soma: " + sum);
        System.out.println("Média: " + average);
    }

}
