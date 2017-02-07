import random
import csv

QueryList = open('QueryList.csv', 'r')
QueryList = csv.reader(QueryList)
QueryList = [row for row in QueryList]
QueryList = [l[0] for l in QueryList]

def Random():
	return random.choice(QueryList)
def Multi():
	return QueryList