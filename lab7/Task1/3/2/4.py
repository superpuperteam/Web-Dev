def string_splosion(str):
  result = ""
  for i in range(len(str)+1):
    for j in range(i):
      result += str[j]
      
  return result