/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    

    let len = nums.length;
    for(let i=0; i<len; i++){
        let k = 0;
        for(let j=0; j<len; j++){
            if(nums[i] == nums[j]){
                k++;
            }
        }
        if(k>1){
            nums.splice(i,k-1);
        }
    }
    return nums.length;
};