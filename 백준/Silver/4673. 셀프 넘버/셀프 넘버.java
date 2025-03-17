import java.util.*;


public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        for(int i = 1;i<10000;i++){
            numbers.add(i);
        }
        int index = 0;
        while (index < numbers.size()) {
            int checkingNum = numbers.get(index);
            while (checkingNum <= 10000) {
                int currentNumber = checkingNum;
                int milion = 0;
                int thousands = 0;
                int hundreds = 0;
                int tens = 0;
                int one = 0;
                if (currentNumber == 10000) {
                    milion = currentNumber / 10000;
                    currentNumber = currentNumber % (milion * 10000);
                }
                if (currentNumber >= 1000) {
                    thousands = currentNumber / 1000;
                    currentNumber = currentNumber % (thousands * 1000);
                }
                if (currentNumber >= 100) {
                    hundreds = currentNumber / 100;
                    currentNumber = currentNumber % (hundreds * 100);
                }

                tens = currentNumber / 10;
                one = currentNumber - (tens * 10);

                int notSelfNumber = checkingNum + milion + thousands + hundreds + tens + one;

                if (numbers.contains(notSelfNumber)) {
                    int numIndex = numbers.indexOf(notSelfNumber);
                    numbers.remove(numIndex);
                }
                checkingNum = notSelfNumber;
            }
            index++;


        }
        for (int i = 1; i <= 10000; i++) {
            if (numbers.contains(i)) {
                System.out.println(i);
            }

        }

    }
}
