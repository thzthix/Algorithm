import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          List<Integer> students = new ArrayList<>();
          for(int i=1;i<= 28 ; i++){
              students.add(scanner.nextInt());
          }
            Collections.sort(students);
          for(int i=1;i<=30;i++){
              if(!students.contains(i)){
                  System.out.println(i);
              }
          }

    }
}
