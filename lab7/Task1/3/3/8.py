def without_end(str):
  word = ""
  for i in range(len(str)-2):
    word += str[i+1]
    
  return word