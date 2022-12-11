import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

y = re.findall("ai", txt)
print(y)

z = re.search("\s", txt)
print(z)