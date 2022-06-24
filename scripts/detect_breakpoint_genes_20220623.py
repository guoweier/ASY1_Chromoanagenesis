# Weier Guo Python
# 06/23/2022

import os, sys, math
from optparse import OptionParser

# Introduction: 
# This is a script for detecting breakpoints inside gene sequences.
# Input:
# 1. GFF file (genes info)
# 2. breakpoints file
# Output:
# A list of breakpoints that are inside gene sequences. 


usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input_file", dest="f", help="input GFF file (gene)")
parser.add_option("-j", "--junction", dest="j", help="input junction file")
parser.add_option("-o", "--output", dest="o", help="output file")

(opt, args) = parser.parse_args()

# open files and set parameters
f = open(opt.f)
j = open(opt.j)
o = open(opt.o, "w")
ohead = "Chrom\tPos\tInGene\tStart\tEnd\tInfo"
o.write(ohead+"\n")
Genes = {}

# put GFF file into dictionary
for line in f:
	if line[0] == "#":
		continue
	else:
		line = line.split("\n")[0]
		ln = line.split("\t")
		if ln[2] == "gene":
			chrm = ln[0]
			start = int(ln[3])
			end = int(ln[4])
			info = ln[8]
			if chrm not in Genes:
				Genes[chrm] = []
			Genes[chrm].append([start,end,info])

# check the breakpoint input file
jhead = j.readline()
for line in j:
	line = line.split("\n")[0]
	ln = line.split("_")
	chrom = ln[0]
	pos = int(ln[1])
	for gene in Genes[chrom]:
		if gene[0] <= pos and gene[1] >= pos:
			text = chrom + "\t" + str(pos) + "\t" + "TRUE" + "\t" + str(gene[0]) + "\t" + str(gene[1]) + "\t" + str(gene[2])
			o.write(text + "\n")

f.close()
j.close()
o.close()






