
import re

text = "I climb to the top of the world!"

x = re.findall("c.*top", text)
print x

x = re.findall("the", text)
print x
