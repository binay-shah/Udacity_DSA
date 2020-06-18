"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

tel_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    


for rec in texts:       
    tel_numbers.add(rec[0])
    tel_numbers.add(rec[1])


for rec in calls:       
    tel_numbers.add(rec[0])
    tel_numbers.add(rec[1])            

print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
