//BufferedReader와 StringTokenizer 사용
// "("가 나올 때까지 일단 다 넣는다
//만약 스택에 있는게 "(" 이고 다음게 ")"이면 pop한다
//stack의 개수가 괄호 개수다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        char[] inputs = bf.readLine().toCharArray();
        Stack<Character> stack = new Stack<>();
        for (char c : inputs) {
            if (!stack.isEmpty() && stack.peek() == '(' && c == ')') {
                stack.pop();
                continue;

            }
            stack.push(c);
        }

        System.out.println(stack.size());

    }


}

