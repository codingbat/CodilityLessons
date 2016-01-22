import java.util.List;
import java.util.ArrayList;

class BinaryGap {
    public int solution(int N) {
        // write your code in Java SE 8
        List<Integer> binary = new ArrayList();
        
        while (N > 0) {
            binary.add(N%2);
            N = N/2;
        }
        
        //System.out.print(binary);
        // int longestGap = 0;
        // for (int i = 0; i < binary.size()-1; i++)
        // {
        //     int gap = 0;
        //     while (i+1 != 1) {
        //         gap++;
        //         i++;
        //     }
            
        //     if(gap>longestGap && binary.get(i-1)==1)
        //         longestGap=gap;
        // }
        
        
        
        return longestGap;
    }
}
