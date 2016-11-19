# IR_task1

** Purpose: **  

Read in a tab delimited document, create invert index file. a program to query the invert index file. 

** Usage ** 

Task 1 <br \> 

```
python3 create_index.py [input document] [output document name]
```

Task 2 <br \>

```
python3 query.py [input document] [invert index file]
```
query.py can continuously querying. Ctrl+C (keyboard interrupt) ends the program. 

** Example ** 

Task 1 <br \>

```
python3 create_index.py tubadw-r1-ir-sample-100000 myindex.txt
```

Task 2 <br \>

```
python3 query.py tubadw-r1-ir-ids-100000 myindex.txt
```

** python library requirements ** 
Python version >= 3.5.1 <br \>
