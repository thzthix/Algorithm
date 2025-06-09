//N을 입력받는다
//k를 입력받는다
//고장난 신호등을 입력받는다
//최소 min = 0;
// 그냥 배얄  0 0 0 1 1 0 0 0 0 0
//누적합 배열
// 고장난 신호등 자리 1을 채운다
//슬라이딩 윈도우 를 하면서
//1의 개수 카운트(구간 누적합을 계산)
//min을 개산한다
//min을 출력한다.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int B = sc.nextInt();
        int min = 999999;
        int[] wrongArray = new int[N];
        int[] S = new int[N];
        for (int i = 0; i < B; i++) {
            int wrong = sc.nextInt();
            wrongArray[wrong - 1] = 1;
        }
        S[0] = wrongArray[0];
        for (int i = 1; i < N; i++) {
            S[i] = S[i - 1] + wrongArray[i];
        }
        for (int i = K; i < N; i++) {
            int j = i - K;
            int numToFix = S[i] - S[j];
            if (min > numToFix) {
                min = numToFix;
            }
        }
        System.out.println(min);

    }
}