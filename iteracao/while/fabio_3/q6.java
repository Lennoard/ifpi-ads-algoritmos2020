public class q6 {

    public static void main(String[] args) {
        System.out.println("TABUADA DOS NÚMEROS DE 1 ATÉ 10");

        for (int n = 1; n <= 10; n++) {
            printTable(n);
        }
    }

    private static void printTable(int n) {
        System.out.println("============");
        for (int i = 0; i <= 10; i++) {
            System.out.printf("%d * %d = %d%n", n, i, n * i);
        }
    }

}
