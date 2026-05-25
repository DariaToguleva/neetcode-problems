class Solution {

    public String encode(List<String> strs) {
        String fin = "";
        for (String str : strs) {
            fin += str.length() + "#" + str;
        }
        return fin;
    }

    public List<String> decode(String str) {
        List<String> fin = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int len = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + len;
            fin.add(str.substring(i, j));
            i = j;
        }
        return fin;
    }
}
