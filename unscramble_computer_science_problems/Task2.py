"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

dict_calls = {}
for rec in calls:
	if dict_calls.get(rec[0]) != None:
		dict_calls[rec[0]] += int(rec[3])
	else:
		dict_calls[rec[0]] = 	int(rec[3])

	if dict_calls.get(rec[1]) != None:
		dict_calls[rec[1]] += int(rec[3])
	else:
		dict_calls[rec[1]] = 	int(rec[3])	
	
list_calls = [ (k, v) for k, v in sorted(dict_calls.items(), key=lambda item: item[1], reverse=True)]

print("{} spent the longest time, {} seconds, on the phone during September 2016.". format(list_calls[0][0], list_calls[0][1]))
    		

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""



