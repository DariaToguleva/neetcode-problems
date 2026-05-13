class Solution {
    public boolean isAnagram(String s, String t) {
        int[] arr = new int[26];
        int[] arr2 = new int[26];

        for (Character ch : s.toCharArray()) {
            arr['z' - ch]++;
        }
        for (Character ch : t.toCharArray()) {
            arr2['z' - ch]++;
        }

        for (int i = 0; i < 26; i++) {
            if (arr[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }
}
