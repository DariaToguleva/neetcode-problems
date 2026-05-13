class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        int n = stones.length;
        for (int stone : stones) {
            heap.offer(stone);
        }

        while(heap.size() > 1){
            int r1 = heap.poll();
            int r2 = heap.poll();
            heap.offer(r1 - r2);
        }
        return heap.peek();
    }
}
