//승환이 앞에 서있는 학생 수 N
//현재 지나가야 하는 자연수 count
//성공여부 isNice
//학생수 bufferedReader랑 StringTokenizer이용해 받는다.
//스택 초기화
//스택에 학생들 넣음 (없으면 무조건 넣음)
//만약 스택.peek()햇는데
//현재 학생보다 peek이 작다면 pop하고 넣는다.
//아니면 그냥 넣느낟.
//만약 pop이 현재 count보다 크다면 isNice = false, sad 프린트하고 종료.
//isNice가 true라면 Nice

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        Stack<Integer> stack = new Stack<>();
        int count = 1;
        for (int i = 0; i < N; i++) {
            int currentNum = Integer.parseInt(st.nextToken());
            if (currentNum == count) {
                count++;
            } else {
                stack.push(currentNum);
            }
            while (!stack.isEmpty() && stack.peek() == count) {
                stack.pop();
                count++;
            }


        }
        if (stack.isEmpty()) {
            System.out.println("Nice");
        } else {
            System.out.println("Sad");
        }


    }

}

