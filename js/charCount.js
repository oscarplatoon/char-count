function charCount(str) {
  var letter_obj = {}
  for (character of str) {
    if (character in letter_obj){
      letter_obj[character] = (letter_obj[character] + 1)
    }
    else {
      letter_obj[character] = 1
    }
  } console.log(letter_obj)
}
charCount('abbc')

// still need to sort
