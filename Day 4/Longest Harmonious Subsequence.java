class Solution {
    public int findLHS(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(!map.contains(i)){
                map.put(i,0);
            }
            else{
                map.put(i,map.get(i)++)
            }
        }
        ans=0
        for(int i=0;i<nums.length;i++){
            if(map.contains(i+1)){
               ans=Math.max(ans,) 
            }
        }
    }
}
