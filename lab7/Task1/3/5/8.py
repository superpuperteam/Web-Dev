def in1to10(n, outside_mode):
  if outside_mode:
    if 1 >= n or n >= 10:
      return True
  
  if not outside_mode and (1 <= n <= 10):
    return True
    
  return False