// N을int로 받는다.
// 자료형 String으로 SnUM을 받는다.
// sNum을 char[] cNum로 바꾼다. toCharArray()
//숫자의 합 sum을 선언한다. 초깃값 0
//for(cNum의 length만큼){
    //sum에 인덱스에 있는 값을 int로 바꿔서 더한다.
//}
//sum을 출력한다.
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        String sNum = scanner.next();
        char[] cNum = sNum.toCharArray();
        int sum = 0;
        for(int i = 0;i<cNum.length;i++){
            sum += cNum[i] - '0';
        }
        System.out.println(sum);
    }
}