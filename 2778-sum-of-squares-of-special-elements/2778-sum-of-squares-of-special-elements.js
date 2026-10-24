/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfSquares = function(nums) {
    
    let s = 0 
    const l = nums.length
    for (let i = 0; i<l;i++){
      if (l%(i+1)==0){
      s+=nums[i]**2
      }
    }
    return s

};