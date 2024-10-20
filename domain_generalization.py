#!/usr/bin/env python3

import sys


print(sys.argv[1], sys.argv[2], sys.argv[3])

def domain_generalization(file_in1, file_in2, file_out):
    with open(file_in1, 'r') as fin1:
        fin1_lines = fin1.read().splitlines()
    with open(file_in2, 'r') as fin2:
        fin2_lines = fin2.read().splitlines()
    with open(file_out, 'w+') as fout:
        cur_domain = ''
        for line in fin1_lines:
            line_tree = line.strip('\n').split('.')
            for n in range(len(line_tree)):
                if n == 0:
                    cur_domain = line_tree[-(n+1)]
                else:
                    cur_domain = line_tree[-(n+1)] + '.' + cur_domain
                    if cur_domain in fin2_lines:
                        print(cur_domain)
                        fout.write(cur_domain)
                        fout.write('\n')
            
if __name__ == '__main__':
    domain_generalization(sys.argv[1], sys.argv[2], sys.argv[3])
