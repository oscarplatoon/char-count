def char_count(str):
  # Split string into a list
  split = list(str)
  # Dictionary of letters
  dict = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0
  }
  # Final answer
  answer = {}
  # Loop through the list and add values to the letters dictionary
  for i in split :
    if i in dict :
      dict[i] += 1
      
  # Remove all letter with the value of 0 and return dictionary
  
  
  
  for x, value in dict.items() :
    if value >= 1 :
      answer[x] = value
      

  return(answer)
