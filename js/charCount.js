
function charCount(str, target) {

    var splitStr = str.split("")
    var charCount = 0
    for (var i of splitStr) {
        if (i == target) {
            charCount++
        }
    }
    return charCount
};


module.exports = charCount;

//console.log(charCount("aaabbc",'a'))//3