/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var calculateScore = function(a, b) {
    const a_bin = a.toString(2).split("1").length-1
    const b_bin = b.toString(2).split("1").length-1

    if (a_bin >= b_bin){
    return a_bin*b_bin
    }
    else{
    return Math.floor(b_bin/a_bin)
    }
    
};