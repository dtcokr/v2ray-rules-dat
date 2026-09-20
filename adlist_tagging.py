#!/usr/bin/env python3

import sys
import re


print(sys.argv[1], sys.argv[2])

tag_pattern = re.compile(r'^\#')
line_pattern = re.compile(r'$')

def tag(file_in, file_out):
    with open(file_in, 'r') as fin:
        lines = fin.readlines()
    with open(file_out, 'w+') as fout:
        for line in lines:
            if re.match(tag_pattern, line):
                # print(line.strip('\n'))
                tag = ',' + line.strip('\n').strip("# ")
            else:
                complete_line = re.sub(line_pattern, tag, line.strip('\n'))
                # print(complete_line.strip('\n'))   
                fout.write(complete_line)
                fout.write('\n')   
            
if __name__ == "__main__":
    tag(sys.argv[1], sys.argv[2])
