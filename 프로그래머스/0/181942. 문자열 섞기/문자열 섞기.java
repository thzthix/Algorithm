class Solution {
    public String solution(String str1, String str2) {
        int fullLength = str1.length() + str2.length();
        String answer = "";
        int str1index = 0;
        int str2index = 0;
        for(int i =0;i<fullLength;i++){

            if(i%2 == 0){
                answer += str1.charAt(str1index);
                str1index++;
                
            }
            else{
                answer+=str2.charAt(str2index);
                str2index++;
            }
        }
        return answer;
    }
}