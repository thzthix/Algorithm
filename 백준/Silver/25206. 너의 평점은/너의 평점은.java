import java.util.*;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        List<Double> scores = new ArrayList<>();
        List<Double> scoremultiplesubject = new ArrayList<>();

        for (int i = 0; i < 20; i++) {
            String input = scanner.nextLine();
            String[] splitted = input.split(" ");
            String stringScore = splitted[2];
            Double number = Double.parseDouble(splitted[1]);
            if (stringScore.equals("P")) {
                continue;
            }
            scores.add(number);
            switch (stringScore) {
                case "A+":
                    scoremultiplesubject.add(number*4.5);
                    break;
                case "A0":
                    scoremultiplesubject.add(number*4.0);
                break;
                case "B+":
                    scoremultiplesubject.add(number*3.5);
                break;
                case "B0":
                    scoremultiplesubject.add(number*3.0);
                    break;
                case "C+":
                    scoremultiplesubject.add(number*2.5);
                break;
                case "C0":
                    scoremultiplesubject.add(number*2.0);
                break;
                case "D+":
                    scoremultiplesubject.add(number*1.5);
                break;
                case "D0":
                    scoremultiplesubject.add(number*1.0);
                break;
                case "F":
                    scoremultiplesubject.add(number*0.0);
                break;
            }

        }
        Double sum = 0.0;
        for(Double score:scores){
            sum+=score;
        }
        Double subjectMultipleSum = 0.0;
        for(Double score: scoremultiplesubject){
            subjectMultipleSum += score;
        }
        System.out.println(subjectMultipleSum / sum);


    }


}

