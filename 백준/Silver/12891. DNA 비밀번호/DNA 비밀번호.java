import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] myArr;
    static int[] checkArr;
    static int numOfSatisfied = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int result = 0;
        myArr = new int[4];
        checkArr = new int[4];
        char[] sentence = new char[S];

        sentence = bf.readLine().toCharArray();
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 4; i++) {
            checkArr[i] = Integer.parseInt(st.nextToken());
            if (checkArr[i] == 0) {
                numOfSatisfied++;
            }
        }
        for (int i = 0; i < P; i++) {
            Add(sentence[i]);
        }
        if (numOfSatisfied == 4) {
            result++;
        }

        for (int i = P; i < S; i++) {
            int j = i - P;
            Add(sentence[i]);
            Remove(sentence[j]);
            if (numOfSatisfied == 4) {
                result++;
            }
        }
        System.out.println(result);
        bf.close();


    }

    public static void Add(char c) {
        switch (c) {
            case 'A':
                myArr[0]++;
                if (myArr[0] == checkArr[0]) {
                    numOfSatisfied++;
                }
                break;
            case 'C':
                myArr[1]++;
                if (myArr[1] == checkArr[1]) {
                    numOfSatisfied++;
                }
                break;
            case 'G':
                myArr[2]++;
                if (myArr[2] == checkArr[2]) {
                    numOfSatisfied++;
                }
                break;
            case 'T':
                myArr[3]++;
                if (myArr[3] == checkArr[3]) {
                    numOfSatisfied++;
                }
                break;
        }
    }

    public static void Remove(char c) {
        switch (c) {
            case 'A':
                if (myArr[0] == checkArr[0]) {

                    numOfSatisfied--;
                }
                myArr[0]--;
                break;
            case 'C':
                if (myArr[1] == checkArr[1]) {
                    numOfSatisfied--;
                }
                myArr[1]--;
                break;
            case 'G':
                if (myArr[2] == checkArr[2]) {
                    numOfSatisfied--;
                }
                myArr[2]--;
                break;
            case 'T':
                if (myArr[3] == checkArr[3]) {
                    numOfSatisfied--;
                }
                myArr[3]--;
                break;
        }
    }
}