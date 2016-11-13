########
# Library
########
import sys
import pandas as pd
import numpy as np
from collections import Counter
##################################################################
# Task : create index
# command : python3 create_index_second.py document_input index_output
# Idea : take lemma and document id, create a list of token for each document (id),  
#        for each lemma token find 
# 
#################################################################

myinput = pd.read_csv(sys.argv[1], sep="\t",header=None,encoding="utf-8")
print("Data read in...")
lemma=myinput.iloc[:,[5,2]]
lemma=lemma.drop_duplicates()
lemma_uniqkey=[key for key in Counter(lemma[lemma.columns[1]]).keys()]
document_id=set(lemma[lemma.columns[0]])
lemma=lemma.sort_values(by=2)
lemma=lemma.reset_index(drop=True)
lemma=lemma.values
my_index=dict()
print("Index creating...")
for w in lemma_uniqkey:
	temp=np.where(lemma==w)
	id_list=[d for d,t in lemma[[temp[0]]]]
	my_index[w]=id_list

print("Writing to your file")
with open(sys.argv[2], 'w') as f:
	for key in my_index.keys():
		value=sorted(my_index[key])
		f.write(key+"\t"+" ".join([str(x) for x in value])+"\n")




