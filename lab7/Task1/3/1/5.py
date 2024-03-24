def parrot_trouble(talking, hour):
  if 7 <= hour <= 20:
    return False
  elif talking != False:
    return True
  return False