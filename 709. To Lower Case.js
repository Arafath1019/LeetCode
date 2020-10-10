/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function(str) {
    let arr = str.split("");
    output = [];
    for (let item of arr){
        temp = item.toLowerCase();
        output.push(temp);
    }
    
    
    result = output.join("");
    return result;
};