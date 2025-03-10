import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          List<Integer> numbers = new ArrayList<>();
          for(int i=0;i<9;i++){
              numbers.add(scanner.nextInt());
          }
          Integer max = Collections.max(numbers);
          int index = numbers.indexOf(max)+1;

          System.out.println(max);
          System.out.println(index);

    }
}
