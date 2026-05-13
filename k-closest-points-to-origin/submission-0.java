class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<List<Double>> heap = new PriorityQueue<>((a, b) -> Double.compare(b.get(0), a.get(0)));
        for(int[] point : points){
            ArrayList<Double> arr = new ArrayList<>();
            arr.add(Math.sqrt(Math.pow(point[0],2) +
                 Math.pow(point[1] ,2)));
            arr.add((double) point[0]);
            arr.add((double) point[1]);
            heap.offer(arr);
            if(heap.size() > k){
                heap.poll();
            }
        }

        int[][] newArr = new int[k][2];
        for(int i = 0; i < k; i++){
            List<Double> p = heap.poll();
            newArr[i][0] = p.get(1).intValue();
            newArr[i][1] = p.get(2).intValue();
        }
        return newArr;
    }
}
