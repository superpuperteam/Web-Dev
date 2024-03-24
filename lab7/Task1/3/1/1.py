def sleep_in(weekday, vacation):
    if (weekday == False and vacation == False) or (weekday == False and vacation == True) or (weekday == True and vacation == True):
        return True
    if weekday == True and vacation == False:
        return False