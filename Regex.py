

import re

mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, Javascript or PHP."

# find for "You"

# matches from the beginning of the string
x = re.match("you", mystr, re.I)

# matches anywhere in the string
# search()
# a = re.search(pattern, string, optional)

arp = "22.22.22.1       0     b4:a9:5a:ff:c8:45      L"

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(a.group(4))




