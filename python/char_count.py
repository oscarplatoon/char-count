# for loop over str
# push to dict as key value 
# if already in dict, increment

def char_count(str):
  letter_dict = {}
  for letter in str:
    if letter.isalpha():
      if letter in letter_dict.keys():
        letter_dict[letter] = (letter_dict[letter] + 1)
      else:
        letter_dict[letter] = 1
    else:
      pass
  print(dict(sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)))
