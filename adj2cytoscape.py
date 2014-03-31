# How to run:
# python adj2cytoscape.py file_input.adj > output_file.txt
# 

#import sys library to get Command-Line Arguments
import sys

f = open(sys.argv[1])
n = 0

#counting lines from inputfile
for line in f:
       if line.strip():
          n += 1
f.close()

f = open(sys.argv[1])
#convert *.adj to input cytoscape
l = f.readlines()
for i in range(19,n):
    columnas = l[i].split('\t')
    j = 0
    while j < len(columnas)-1:
        source = columnas[0]
        gen_target=columnas[j+1]
        mi = columnas[j+2]
        print "%s %s %s" % (source, gen_target, mi)
        j+=2
f.close()
