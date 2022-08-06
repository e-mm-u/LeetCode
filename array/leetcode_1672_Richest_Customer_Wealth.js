var accounts = [[1,2,3],[3,2,1]];

var l = accounts.length;
// console.log(l);
var wealth = [];
// console.log(wealth);

for(var i=0;i<l;i++){
    var array = accounts[i];
    // console.log(array);

    var sum = array.reduce((a, b) => a + b, 0);
    // console.log(sum);

    wealth.push(sum);
    // console.log(wealth);
}
console.log(Math.max(...wealth));
return Math.max(...wealth);