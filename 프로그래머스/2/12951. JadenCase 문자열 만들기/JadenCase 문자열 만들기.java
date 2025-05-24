class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ",-1);
        for(int i = 0;i<arr.length;i++){
            String current = arr[i];
            if(current.length() == 0){
                continue;
            }
            char [] str = current.toCharArray();
             char first = str[0];
            if( Character.isLetter(first)){
            first = Character.toUpperCase(first);
            str[0] = first;
            for(int j = 1;j<str.length;j++){
                char letter = Character.toLowerCase(str[j]);
                str[j] = letter;
            }
                
            }else{
                            for(int j = 0;j<str.length;j++){
                char letter = Character.toLowerCase(str[j]);
                str[j] = letter;
            }
                
            }
            

            arr[i] = new String(str);
        }
        return String.join(" ",arr);
    }
}