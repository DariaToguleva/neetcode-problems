class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> sets = new HashSet<>();
        
        int i = 0;
        int max = 0;

        for (int j = 0; j < s.length(); j++) {
            while (sets.contains(s.charAt(j))) {
                sets.remove(s.charAt(i));
                i++;
            }
            sets.add(s.charAt(j));
            max = Math.max(max, j - i + 1);
        }
        return max;
    }
}
