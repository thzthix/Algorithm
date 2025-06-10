import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        int num = 1;
        boolean possible = true;
        StringBuffer bf = new StringBuffer();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            int n = A[i];
            if (n >= num) {
                while (n >= num) {
                    stack.push(num++);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            } else {
                int pop = stack.pop();
                if (pop > n) {
                    System.out.println("NO");
                    possible = false;
                    break;
                } else {
                    bf.append("-\n");
                }
            }
        }
        if (possible) System.out.println(bf);
    }

}

