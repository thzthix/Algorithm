import java.util.*;
public class Main{
    public static void main(String[] args){
        //int N을 받고
        //sum,count, startIndex, endIndex 초기화
        //while(sum != N)
        //{
        //  sum == N endIndex++, sum +=endIndex, count++
        //  sum < N endIndex++, sum+=endIndex
        //  sum > N sum -= startIndex; startIndex++;
       
        //}
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int sum = 1;
        int count = 1;
        int startIndex = 1;
        int endIndex = 1;
        while(endIndex!=N){
            if(sum == N){
                endIndex++;
                sum+=endIndex;
                count++;
            }
            else if (sum < N){
                endIndex++;
                sum+=endIndex;
            }
            else if (sum > N){
                sum -= startIndex;
                startIndex++;
            }
        }
        System.out.println(count);
        
    
    }
}