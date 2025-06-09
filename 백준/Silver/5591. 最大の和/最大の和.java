//슬라이딩 윈도우
//수의 개수 N을 받는다.
//윈도우의 수 K를 받는다.

//최대값 max 초기화, 누적합 배열S[i] 초기화, 숫자 배열 초기화

//N의 개수만큼 숫자 받아서,누적합 배열에 넣는다.
//수를 누적합을 윈도우에 넣고 맨 앞 원소 누적합을 뺀다.

// 2 5 -4 10 3
// 2 7 3 13 16

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int max = 0;
        int[] S = new int[N];
        for (int i = 1; i <= N - 1; i++) {
            S[i] = S[i - 1] + Integer.parseInt(String.valueOf(sc.nextInt()));
        }
        for (int i = K; i < S.length; i++) {
            int j = i - K;
            int sum = S[i] - S[j];
            if (sum > max) {
                max = sum;
            }

        }
        System.out.println(max);

    }
}