/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var runningSum = function(nums) {
    
    var ans = [];
    ans.push(nums[0]);
    l = nums.length;

    for(var i=1;i<l;i++){
        ans.push(ans[i-1]+nums[i])
    }
        
    return ans;
    
};