class Solution {
    public boolean solution(String s) {
        boolean isNum = true;
        char[] arr = s.toCharArray();
        int len = s.length();
        if(len!=4 && len !=6){
            return false;
        }
        for(int i = 0;i<arr.length;i++){
            if(!Character.isDigit(arr[i])){
                isNum = false;
                break;
            }
        }
        return isNum;
    }
}