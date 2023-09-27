second = input("Enter an integer for seconds:")
minutes = second / 60
seconds = second % minutes
print(second, "seconds is", round(minutes), minutes, "minutes and", seconds, "seconds")