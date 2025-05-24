class Solution {
    public int solution(String t, String p) {
        int pLength = p.length();
        long pValue = Long.parseLong(p);
        int count = 0;

        for (int i = 0; i <= t.length() - pLength; i++) {
            String sub = t.substring(i, i + pLength);
            long subValue = Long.parseLong(sub);
            if (subValue <= pValue) {
                count++;
            }
        }

        return count;
    }
}
