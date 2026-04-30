class Solution {
    public int myAtoi(String s) {
        long x = 0;
        int sign = 1;
        boolean found = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c > 47 && c < 58) {
                found = true;
                x = 10 * x + ((int) c - 48);
                if (x * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;
                if (x * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;
            } else if (c == '-') {
                if (found) {
                    break;
                }
                found = true;
                sign *= -1;
            } else if (c == ' ') {
                if (found) {
                    break;
                }
            } else if (c == '+') {
                if (found) {
                    break;
                }
                found = true;
            } else {
                break;
            }
        }
        return (int) x * sign;
    }
}