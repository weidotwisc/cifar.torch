#!/usr/bin/env python
import sys
step = int(sys.argv[1])
index = 0
with open("log.stdout", 'r') as f:
    for line in f.readlines():
        if "Train accuracy" in line:
            index += 1
            if index % step != 0:
                continue
            print(line.split("%")[0].split(" ")[-2].strip())
