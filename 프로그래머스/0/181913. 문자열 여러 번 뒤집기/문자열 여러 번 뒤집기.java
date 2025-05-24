class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(my_string);
        for(int i=0;i<queries.length;i++){
            int[] arr = queries[i];
            int start = arr[0];
            int end = arr[1];
            String substr = sb.substring(start,end+1);
            StringBuilder sb2 = new StringBuilder(substr);
            sb2.reverse();
            sb.replace(start,end+1, sb2.toString());
            
        }
        return sb.toString();
    }
}