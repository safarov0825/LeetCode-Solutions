class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romans = new HashMap<>();
        romans.put('I', 1);
        romans.put('V', 5);
        romans.put('X', 10);
        romans.put('L', 50);
        romans.put('C', 100);
        romans.put('D', 500);
        romans.put('M', 1000);

        int number = 0;
        char[] digits = s.toCharArray();
        int previous = romans.get(digits[digits.length - 1]);
        for (int i = digits.length - 1; i >= 0; i--) {
            int digit = romans.get(digits[i]);
            if (previous <= digit) {
                number += digit;
            } else {
                number -= digit;
            }
            previous = digit;
        }
        return number;
    }
}