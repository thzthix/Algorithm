import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = Integer.parseInt(scanner.nextLine().trim()); // 테스트 케이스 개수

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(scanner.nextLine().trim());

            if (N == 0) {
                System.out.println("Case #" + (i + 1) + ": INSOMNIA");
                continue;
            }

            Set<Integer> seenDigits = new HashSet<>();
            int multiple = 0;
            int currentNumber = 0;

            while (seenDigits.size() < 10) {  // 0~9 모든 숫자가 나올 때까지 반복
                multiple++;
                currentNumber = multiple * N;

                // 현재 숫자의 각 자릿수를 Set에 추가
                int temp = currentNumber;
                while (temp > 0) {
                    seenDigits.add(temp % 10);
                    temp /= 10;
                }
            }

            System.out.println("Case #" + (i + 1) + ": " + currentNumber);
        }
    }
}
