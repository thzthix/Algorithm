import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] sd1 = {1,2,3,4,5};
        int[] sd2 = {2,1,2,3,2,4,2,5};
        int[] sd3 = {3,3,1,1,2,2,4,4,5,5};
        
        int count1 = 0;
        int count2 = 0;
        int count3 = 0;
        
        for(int i = 0; i<answers.length;i++){
            if(answers[i] == sd1[i%5]){
                count1++;
            }
            if(answers[i] == sd2[i%8]){
                count2++;
            }
            if(answers[i] == sd3[i%10]){
                count3++;
            }

            
        }
         int max = Math.max(count1,count2);
            max = Math.max(max,count3);
        List<Integer> arr = new ArrayList<>();
       
            if(max == count1){
                arr.add(1);
            }
            if(max == count2){
                arr.add(2);
            }
            if(max == count3){
                arr.add(3);
            }
        
        int[] results = new int [arr.size()];
        for(int i = 0;i<results.length;i++){
            results[i] = arr.get(i);}
        return results;
        }
        
        
    }
