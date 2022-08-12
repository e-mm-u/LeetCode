/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
 var shuffle = function(nums, n) {
    
    const n1 = nums.splice(0,n);
    const n2 = nums.splice(-n);
    const ans = [];
    for(let i=0;i<n;i++){
        ans.push(n1[i]);
        ans.push(n2[i]);
    }
    return ans;
};