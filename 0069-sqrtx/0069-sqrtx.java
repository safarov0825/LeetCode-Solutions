class Solution {
    public int mySqrt(int x) {
        int num = 1;
        while (num <= x / num) {
            num++;
        }

        return num - 1;
    }
}