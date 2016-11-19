########
# Library
########
import sys
import csv
from collections import defaultdict
##################################################################
# Task : create index
# command : python3 create_index_second.py document_input index_output
# Idea : take lemma and document id, create a dictionary, add the key,value if the key does not exist
# add the value if the key exist  
#################################################################
print("Data read in...")

myinput=list()
with open(sys.argv[1],"r") as f:	
	for l in f: 
		mycols=l.split("\t")
		if len(mycols)>1:
			temp=tuple([mycols[2],int(mycols[5])])
			myinput.append(temp)
print("Create index...")
myinput=set(myinput)
myinput_dict=defaultdict(list)
for v,t in myinput:
	myinput_dict[v].append(t)
		
with open(sys.argv[2],"w") as myout:
	writer = csv.writer(myout,delimiter='\t')
	for key, value in myinput_dict.items():
		valueout=[" ".join(str(x) for x in value)]
		writer.writerow([key] + valueout)
