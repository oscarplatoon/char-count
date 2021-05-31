def char_count(str_input):
  # Your code here
  """
  create empty dict and list
  split string into list to get list of chars
  replace method to remove whitespace if it exists
  """
  output = {}
  str_list = []
  str_list[:] = str_input.replace(" ", "")

  """
  loop through list
  if l is in dict then add 1 to key value
  if not update and initialize key value to 1
  """
  for l in str_list:
    if l in output:
      output[l] += 1
    else:
      output.update({l: 1})
  
  return output