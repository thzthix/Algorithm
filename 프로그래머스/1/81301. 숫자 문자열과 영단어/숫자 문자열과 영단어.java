import java.util.*;

class Solution {
    public int solution(String s) {
        String[] numbers = {"zero","one","two","three","four","five","six","seven","eight","nine","ten"};
        for(int i = 0;i<numbers.length;i++){
            s = s.replace(numbers[i],String.valueOf(i));
        }
        return Integer.parseInt(s);
    }
}
