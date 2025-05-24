class Solution {
    public int solution(String s) {
      int i = 0;
        int count = 0;
        while(i<s.length()){
            char c = s.charAt(i);
            int j = i+1;
            int snum = 1;
            int nsnum = 0;
            while(j<s.length()){
                char c1 = s.charAt(j);
                if(c1 == c){
                    snum++;
                }
                else{
                     nsnum++;
                }
               
                if(snum == nsnum){
                    break;
                }
                j++;
                
            }
                                count++;
                    i = j+1;
        }
        return count;
    }
}
