class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> str1 = new HashMap<>();
        HashMap<Character, Integer> str2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            str1.put(s.charAt(i), str1.getOrDefault(s.charAt(i), 0) + 1);
            str2.put(t.charAt(i), str2.getOrDefault(t.charAt(i), 0) + 1);
        }

        for (Character key : str1.keySet()) {
            if (!str2.containsKey(key) || !str1.get(key).equals(str2.get(key))) {
                return false;
            }
        }
        return true;
    }
}
