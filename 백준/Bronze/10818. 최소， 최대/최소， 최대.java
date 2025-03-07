import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine();
        int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int max = numbers[0];
        int min = numbers[0];
        for (int i=1;i<=numbers.length-1;i++){
            int currentNumber = numbers[i];
            if(currentNumber > max){
                max = currentNumber;
            }else if (currentNumber  < min){
                min = currentNumber;
            }

        }
        System.out.println(min+" "+max);




    }
}
