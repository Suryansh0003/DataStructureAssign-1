def WordsCounter(string):
    count = 0
    # Also use  return len(string)
    for i in string:
        count += 1
    return count


string = "pwskills"
print("Count - ", WordsCounter(string))
