import re

str = '44000000000'
x = re.search('\D', str)
print(x == None)