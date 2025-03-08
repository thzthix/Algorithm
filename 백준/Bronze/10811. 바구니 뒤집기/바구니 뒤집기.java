import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        int[] buckets= new int[N];
        for(int i = 0; i<N; i++){
            buckets[i] = i+1;
        }
        for(int i = 0; i< M; i++){
            int start = scanner.nextInt();
            int end = scanner.nextInt();

            int currentStart =start-1;
            int currentEnd = end-1;

            while(currentStart<currentEnd){
                int temp = buckets[currentStart];
                buckets[currentStart] = buckets[currentEnd];
                buckets[currentEnd] = temp;
                currentStart++;
                currentEnd--;
            }



            }


        for(int i = 0; i < N; i++){
            System.out.print(buckets[i] +" ");
        }


    }
}
