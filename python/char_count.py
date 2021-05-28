def char_count(str):
  
  
  # create a DICTIONARY to store CHAR counts
  char_count_dictionary = {}
  
  

  # Remove spaces from STR and convert to lower case
  str = str.replace(" ", "").lower()

  # for each CHAR in STR if CHAR is not in DICTIONARY add CHAR as key and set value to 1
  # else add 1 to CHAR's value in dictionary
  for char in str:
    if char in char_count_dictionary:
      char_count_dictionary[char] += 1
    else:
      char_count_dictionary[char] = 1
  
  # sort the dictionary by value
  char_count_dictionary = dict(sorted(char_count_dictionary.items(), key= lambda item:item[1], reverse=True))
  
  # return the sorted dictionary 
  return char_count_dictionary

 
print(dict(char_count("an apple a day will keep the doctor away")))