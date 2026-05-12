class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        char[] letters = s.toCharArray();
        for (int i = letters.length - 1; i >= 0; i--) {
            if (letters[i] == ' ') {
                if (count == 0) {
                    continue;
                }
                break;
            }
            count++;
        }

        return count;
    }
}