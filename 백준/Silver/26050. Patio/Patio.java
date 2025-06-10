//빨 1*1
//파란색 8개 1*4+4  = 9
//1+9 = 10

//빨간색 2*2개
//파란색 2*4+4  =12
//4+16 = 20

//3*3개
//4(3+1) = 16 + 9 = 25


//윈도우 크기 n일때, 한 변에 바깥 타일이 n의 루트 p개 있다.
//이 때, 안쪽 타일은 (p-2)^2개 존재해야 하고,
//바깥 타일은 4(p-1)개 존재해야 함.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//문자열 개수 N(int) 입력받는다
//bufferedReader로 파일 입력받는다. toCharArray()
//count 초기화(만들 수 있는 타일 개수)
// 가져야 할 o개수, x개수 배열 [2]
//현재 o개수, x개수 배열 [2]
//가장 가까운 제곱수를 찾는다 = 윈도우 크기 = 9이상
//처음에 윈도우 크기만큼 돌면서 currentHave에 넣어준다.
//만약 개수 총족되면 count++
//캐릭터 add, remove하면서
//개수 맞는지 확인
public class Main {
    static int[] mustHave;
    static int[] currentHave;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.parseInt(bf.readLine());
        char[] s = bf.readLine().toCharArray();
        count = 0;
        mustHave = new int[2]; // 4*(p-1)개이거나, (p-2)^2개이거나
        currentHave = new int[2]; //파란색 0, 빨간색 1
        int p = (int) Math.sqrt(N);
        for (int k = p; k >= 3; k--) {
            int windowSize = (int) Math.pow(k, 2);
            mustHave[0] = 4 * (k - 1); //바깥
            mustHave[1] = (int) Math.pow(k - 2, 2); //안쪽
            currentHave = new int[2];
            for (int i = 0; i < windowSize; i++) {
                Add(s[i]);
            }
            Validate();
            for (int i = windowSize; i < s.length; i++) {
                int j = i - windowSize;
                Add(s[i]);
                Remove(s[j]);
                Validate();
            }
        }
        System.out.println(count);


    }

    public static void Add(char c) {
        switch (c) {
            case 'X':
                currentHave[0]++;
                break;
            case 'O':
                currentHave[1]++;
                break;
        }
    }

    public static void Remove(char c) {
        switch (c) {
            case 'X':
                currentHave[0]--;
                break;
            case 'O':
                currentHave[1]--;
                break;
        }
    }

    public static void Validate() {
        int blue = currentHave[0];
        int red = currentHave[1];
        if ((blue == mustHave[0] && red == mustHave[1]) ||
                (red == mustHave[0] && blue == mustHave[1])) {
            count++;
        }
    }

}

