const charCount = str => {
  //omit space in string
  let string = str.split(' ').join('');
 //create result object
  let letterCountsObj = {}
  // iterate throught string
    for (let i = 0; i < string.length; i++) {
      let currentLetter = string[i];
   // in each letter see if the theres existing key at same index letter
      if (letterCountsObj[currentLetter]) {
        // increment number of occurence value by 1
        // save number of occurence value to new object
        letterCountsObj[currentLetter]++;
      } else {
        // if there no existing key 
        //  value = 1
        letterCountsObj[currentLetter] = 1;
      }
    }
    return letterCountsObj;
};
module.exports = charCount;
