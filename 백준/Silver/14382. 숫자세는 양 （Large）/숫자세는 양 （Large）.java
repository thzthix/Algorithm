import java.util.*;


public class Main {
    public static void main(String[] args) {


        Scanner scanner = new Scanner(System.in);
        int cases = Integer.parseInt(scanner.nextLine().trim());
        for(int i = 1;i<=cases;i++){
            boolean canSleep = false;
            int N = Integer.parseInt(scanner.nextLine().trim());
            int answer = 0;
            if(N == 0){
                System.out.printf("Case #%d: INSOMNIA%n",i);
                continue;
            }
            List<Integer> numbers = new ArrayList<>();
            int count = 0;
            while(!canSleep){
                int currentN = N*(++count);
               int currentNumber  = currentN;
                while(currentNumber>0){
                    int digitNum = currentNumber % 10;
                    currentNumber /= 10;

                    if(!numbers.contains(digitNum)){
                        numbers.add(digitNum);
                    }
                    if(numbers.size()==10){
                        canSleep = true;
                        answer = currentN;
                        break;
                    }
                    if(currentNumber <= 0){
                        break;
                    }


                }
            }
            System.out.println(String.format("Case #%d: %d",i,answer));
        }

    }
}
