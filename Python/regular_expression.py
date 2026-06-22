import re

x = ('the rain in spain')
# to find if the tatement starts with the and ends with rain
y = re.search('^the.*spain$', x)

if y:
    print("Yes, there is at least one match")
else:
    print("No match")