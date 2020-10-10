/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let stringS = s.replace(/[^\w]/g, "").toLowerCase().split("").sort().join("");
    let stringT = t.replace(/[^\w]/g, "").toLowerCase().split("").sort().join("");
    
    if (stringS === stringT){
        return true;
    }else{
        return false;
    }
};
