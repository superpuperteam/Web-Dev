def caught_speeding(speed, is_birthday):
  n = 0
  if is_birthday:
    n = 5
  
  if speed <= 60 + n:
    return 0
  elif speed <= 80 + n:
    return 1
  else:
    return 2