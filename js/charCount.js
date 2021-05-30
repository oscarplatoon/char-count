
const charCount = str => {
  
// declare an output directory that is empty
//remove all spaces from the input string string
//convert all characters to lowercase
//sort the string a - z

  let outputDir = {

    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
    'e' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'i' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0,
    'n' : 0,
    'o' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0,
  }

  let strLowerJoined= str.toLowerCase().replace(" ", ""); 

  for (i in strLowerJoined){
    outputDir[strLowerJoined[i]]+= 1;
  }

  for (j in outputDir){
    if (outputDir[j]==0){
      delete outputDir[j];
    }
  }
  return outputDir;
 

  }


exports.charCount = charCount;












