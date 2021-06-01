def char_count(str):
  output = {}
  for c in str.replace(' ',''):
    if c in output.keys():
      output[c] += 1
    else:
      output[c] = 1
  return(output)
