def alarm_clock(day, vacation):
  if vacation and (day == 6 or day == 0):
    return "off"
  elif vacation or day == 6 or day == 0:
    return "10:00"
  else:
    return "7:00"