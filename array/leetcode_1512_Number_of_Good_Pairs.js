/**
 * @param {number[]} nums
 * @return {number}
 */
 var numIdenticalPairs = function(nums) {
    
    let len = nums.length;
    let pairs = 0;
    
    for(let i=0;i<len-1;i++){
        for(j=i+1;j<len;j++){
            if(nums[i]==nums[j]){
                pairs++;
            }
        }
    }
    return pairs
};
// console.log(numIdenticalPairs( [1,1,1,1]))
