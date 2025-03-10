import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          int[] pieces = {1,1,2,2,2,8};
          for(int i = 0;i<6;i++){
              int number = scanner.nextInt();
              System.out.print(pieces[i] - number+ " ");
          }

    }
}
