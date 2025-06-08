import java.util.*;

public class Main {
  public static void main(String args[]) {
   
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    scanner.nextLine();
    String scores = scanner.nextLine();
    double[] scoresArray = Arrays.stream(scores.split(" ")).mapToDouble(Double::parseDouble).toArray();
    double avg = 0;
    double max = Arrays.stream(scoresArray).max().getAsDouble();
    for(double score: scoresArray){
        avg += (score / max * 100);
    }
    avg = avg / N;
    System.out.println(avg);
}

}