import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int quizNum = Integer.parseInt(stringTokenizer.nextToken());
        long[] S = new long[N+1];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for(int i = 1;i<=N;i++){
            int a = Integer.parseInt(stringTokenizer.nextToken());
            S[i] = S[i-1] + a;
        }
        for(int i = 0; i<quizNum;i++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());
            System.out.println(S[end] - S[start-1]);
        }
        
    }
}