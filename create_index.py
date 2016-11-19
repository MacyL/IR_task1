########
# Library
########
import sys
import csv
from collections import defaultdict
##################################################################
# Task : create invert index. 
# command : python3 create_index.py document_input index_output
#################################################################
print("Data read in...")
# read in data, only need two columns, skip blank line
myinput=list()
with open(sys.argv[1],"r") as f:	
	for l in f: 
		mycols=l.split("\t")
		if len(mycols)>1:
			temp=tuple([mycols[2],int(mycols[5])])
			myinput.append(temp)
			
# go through each element in input list, add the unique token as key, extend value list. 
print("Create index...")
myinput=set(myinput)
myinput_dict=defaultdict(list)
for v,t in myinput:
	myinput_dict[v].append(t)

# formatting output. 		
with open(sys.argv[2],"w") as myout:
	writer = csv.writer(myout,delimiter='\t')
	for key, value in myinput_dict.items():
		valueout=[" ".join(str(x) for x in value)]
		writer.writerow([key] + valueout)
