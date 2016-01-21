// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class BinaryGap {
    public int solution(int N) {
        // write your code in Java SE 8
        List<Integer> binary = new ArrayList();
        
        while (N > 0) {
            binary.add(N%2);
            N = N/2;
        }
        
        System.out.print(binary);
        
        for (int i = 0; i < binary.length(); i++) {
            if 
        }
        
        return 0;
    }
}
