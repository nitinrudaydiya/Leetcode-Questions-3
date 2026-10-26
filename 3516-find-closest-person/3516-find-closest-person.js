/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {
    xc = Math.abs(z-x)
    yc = Math.abs(z-y)
    if (xc<yc){
        return 1
    }
    else if (xc>yc){
      return 2
    }
    else{
      return 0}
    };