#!/usr/bin/env python
#
# Convert contrast curve into portable graymap (PGM) file.
#

import sys
import re

if len(sys.argv) != 2:
    print("Usage: %s PATH_TO_CURVE" % (sys.argv[0]))
    exit(1)

values = []
with open(sys.argv[1]) as f:
    data = f.read()
    for v in data.split(","):
        m = re.search("(\d+\.\d+)f?", v)
        if m:
            values.append(float(m.group(1)))

print("P2 %d 1 255" % (len(values)))
print(" ".join(["%d" % (int(x * 255)) for x in values]))
