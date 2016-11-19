##########
# library
##########
import sys
import csv
from operator import and_
from functools import reduce
from time import sleep
############################################################################
# task : read in queries and get the document id which contains both queries  
############################################################################

# check document id
Document=dict()
with open(sys.argv[1],"r") as f:
	reader=csv.reader(f,delimiter='\t')
	for row in reader:
		Document[int(row[0])]=row[1]

print("Reading index...please wait")

# index file 
myindex_dict=dict()
with open(sys.argv[2],"r") as f_index:
	myindex=[line.rstrip('\n') for line in f_index]
	for i in myindex:
		key=i.split("\t")[0]
		value=i.split("\t")[1]
		values=[v for v in value.split(" ")]
		myindex_dict[key]=values

print("Ready for query!")
try:
	while True : 
		d_id_list=[]
		query=input("Search term : ")
		for e in query.split(" "):
			d_id=myindex_dict[e]
			d_id_list.append(d_id)
	
		tran=[set(v) for v in d_id_list]
		intersect_tran=sorted(set.intersection(*tran))
		if len(intersect_tran) ==0:
			print("No Document is found! Please try again!")
			sleep(0.5)
		else:		
			temp=[]
			for v in intersect_tran: 
				D_name=Document[int(v)]
				temp.append([(int(v),D_name)])			
				print("%d:%s" % (int(v), D_name))
			sleep(0.1)

except KeyboardInterrupt:
	print("\n"+"Program ended, goodbye!")



	




