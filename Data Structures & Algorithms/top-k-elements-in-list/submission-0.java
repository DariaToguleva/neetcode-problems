class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] arr = new List[nums.length + 1];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = new ArrayList<>();
        }
        
        for (Map.Entry<Integer, Integer> ent : freq.entrySet()) {
            arr[ent.getValue()].add(ent.getKey());
        }

        int[] fin = new int[k];
        int index = 0;

        for (int i = arr.length - 1; i > 0 && index < k; i--) {
            for (int n : arr[i]) {
                fin[index++] = n;
                if (index == k) {
                    return fin;
                }
            }
        }
        return fin;
    }
}
