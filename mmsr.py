import csv
import os, fnmatch

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            #return os.path.join(root, name)
            return True

with open('/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/training/acousticbrainz-mediaeval2017-tagtraum-train.tsv','rb') as tsvin, open('new.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout, delimiter=',')
    
    for row in tsvin:
    	name = row[0]+'.json'
    	boolFind = find(name, '/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/')
    	if boolFind:
    		print([row[0]])
    		csvout.writerow([row[0]])

# boolFind = find('1a00a335-fead-46ec-8d4f-06e8341291ea.json', '/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/')
# if boolFind:
# 	print(boolFind)