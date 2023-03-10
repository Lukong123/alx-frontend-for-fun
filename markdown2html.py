#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
'''


import sys
import os.path

if __name__ == '__main__':

    n = len(sys.argv)

    if n < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    
    with open(sys.argv[1], 'r') as markdown:
        c = markdown.readlines()

        for line in c:
            c = c.replace('#', '<h1>')
            
    f2 = open(sys.argv[2], 'w')
    for line in f1:
        f2.write(line)

