import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        Map<Integer, Integer> bucket = new HashMap<>();


        for (int i=0;i<M;i++){
            int start = scanner.nextInt();
            int end = scanner.nextInt();
            int number = scanner.nextInt();

            for(int j = start;j<=end;j++){
                if(!bucket.containsKey(j)){
                    bucket.put(j, number);
                }
                else{
                    bucket.replace(j, number);
                }

            }


        }
        for(int n=1;n<=N;n++){
            if(!bucket.containsKey(n)){
                System.out.print(0);
            }
            else{
                System.out.print(bucket.get(n));
            }
            System.out.print(" ");
        }




    }
}
