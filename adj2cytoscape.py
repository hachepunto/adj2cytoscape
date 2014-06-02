import argparse

parser = argparse.ArgumentParser(description='Convert aracne2 adjacency files to tab separated values suitable for cytoscape.')
parser.add_argument('adj', type=argparse.FileType('r'), nargs="+", help="One or more ADJ files." )
args    = parser.parse_args()

for f in args.adj:
       lineas = f.readlines()       
       for l in lineas:
              if not l.startswith('>'):
                     columnas = l.split('\t')
                     j = 0
                     while j < len(columnas)-1:
                            source     = columnas[0]
                            gen_target = columnas[j+1]
                            mi         = columnas[j+2]
                            print "%s %s %s" % (source, mi, gen_target)
                            j+=2

