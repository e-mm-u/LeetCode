var buildArray = function(nums) {
    var ans = [];
    var l = nums.length;
    for(var i=0;i<l;i++){
        var x = nums[nums[i]];
        ans.push(x);
    }
    return ans;
};