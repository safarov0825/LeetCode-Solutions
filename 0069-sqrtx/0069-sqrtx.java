class Solution {
    public int mySqrt(int x) {
        int i = 0;
        int num = 1;
        while (num <= x / num) {
            i++;
            num++;
        }

        return i;
    }
}