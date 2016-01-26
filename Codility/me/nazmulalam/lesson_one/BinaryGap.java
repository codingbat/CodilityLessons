import java.util.List;
import java.util.ArrayList;

class Solution {
    public int solution(int N) {
        // write your code in Java SE 8
        List<Integer> binary = new ArrayList();
        
        while (N > 0) {
            if (N % 2 == 1 || binary.size() > 0) 
                binary.add(N%2);
                N = N/2;
        }
        
        // System.out.print(binary);
        int longestGap = 0;
        for (int i = 0; i < binary.size()-1; i++)
        {
            int gap = 0;
            if (i == 1) {
                while (i+1 == 0) {
                    gap++;
                    i++;
                }
            }
            
            if(gap>longestGap)
                longestGap=gap;
        }
        
        
        
        return longestGap;
    }
}
