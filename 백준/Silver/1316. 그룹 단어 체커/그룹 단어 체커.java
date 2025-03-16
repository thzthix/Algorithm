import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        int count = 0;

        for(int i =0;i<N;i++){
            String word = scanner.nextLine();
            boolean isGroup = true;
            String[] letters = word.split("");
            for(int j =0;j< letters.length;j++){
                String currentLetter = letters[j];
                String subwords = word.substring(0,j);
                if(subwords.contains(currentLetter)){
                    int previousIndex = subwords.lastIndexOf(currentLetter);
                    if(previousIndex != j-1){
                        isGroup = false;
                        break;
                    }
                }


            }
            if(isGroup){
                count++;
            }

        }
        System.out.println(count);

    }
}

