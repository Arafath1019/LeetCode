/**
 * @param {string} text
 * @return {string}
 */
var arrangeWords = function(text) {
    let x1 = text.split(" ");
    let x2 = x1[0].split("");
    let x3 = x2[0].toLowerCase();
    x2[0] = x3;
    x1[0] = x2.join("");
    
    x1.sort((function(a, b){
          // ASC  -> a.length - b.length
          // DESC -> b.length - a.length
          return a.length - b.length;
        }));

    let y1 = x1[0].split("");
    y1[0] = y1[0].toUpperCase();
    y1 = y1.join("");
    x1[0] = y1;
    return x1.join(" ");
    
    
};