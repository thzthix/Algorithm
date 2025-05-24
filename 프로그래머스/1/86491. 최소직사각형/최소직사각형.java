import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int vmax = 0;
        int hmax = 0;
        for(int i = 0;i<sizes.length;i++){
            int v = Math.max(sizes[i][0], sizes[i][1]);
            int h = Math.min(sizes[i][0],sizes[i][1]);
            
            vmax = Math.max(vmax,v);
            hmax = Math.max(hmax,h);
        }
        return vmax*hmax;
    }
}