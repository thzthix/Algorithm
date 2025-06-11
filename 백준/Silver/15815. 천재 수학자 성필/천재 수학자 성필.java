//BufferedReader와 StringTokenizer 사용
//연산자가 나올때까지 넣는다.
//만약 연산자라면
//숫자를 두개 pop해서 계산해준다. (마지막에 꺼낸게 앞이 된다.)

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        char[] inputs = bf.readLine().toCharArray();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < inputs.length; i++) {
            char current = inputs[i];
            if (!Character.isDigit(current)) {
                int last = Integer.parseInt(String.valueOf(stack.pop()));
                int first = Integer.parseInt(String.valueOf(stack.pop()));
                int result = calculate(current, first, last);
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(String.valueOf(current)));
            }

        }
        System.out.println(stack.pop());
    }

    public static int calculate(char c, int first, int last) {
        switch (c) {
            case '+':
                return first + last;
            case '-':
                return first - last;
            case '*':
                return first * last;
            case '/':
                return first / last;
        }
        return 0;
    }


}

