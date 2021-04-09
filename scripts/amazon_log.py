# Given a log file, create a parser to output line by line, and report the following
#
# - do not output blank lines
# - lines without timestamp
# - lines with timestamp, remove the date
# - display total number of blank lines
# - display total of lines without timestamp
#
# [2020-02-15 12:33:06.755], WARNING: low resources
#
# [2020-02-15 12:33:06.755], INFO: system ok
#
# 440: network packet lost
#
# [2020-02-15 12:33:06.755], WARNING: low resources

import re

log = "./amazon_log.log"

blank = 0
nostamp = 0

f = open(log)
l = f.readline()

while l:
    # count blank lines
    if (l=="\n"):
        blank = blank+1
    # count lines without timestamp
    elif (not re.match("\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}]", l)):
        nostamp = nostamp+1
    # removes the date from lines with timestamp
    elif (re.match("\[\d{4}-\d{2}-\d{2}", l)):
        l = re.sub("\[\d{4}-\d{2}-\d{2} ", "[", l.strip())
        print(l)

    l = f.readline()

print("Total blank lines: {0}".format(blank))
print("Total lines without timestamp: {0}".format(nostamp))
f.close()
