import csv
import os, fnmatch
import json
from pprint import pprint

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            #return os.path.join(root, name)
            return True

# with open('/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/training/acousticbrainz-mediaeval2017-tagtraum-train.tsv','rb') as tsvin, open('new.csv', 'wb') as csvout:
#     tsvin = csv.reader(tsvin, delimiter='\t')
#     csvout = csv.writer(csvout, delimiter=',')
    
#     for row in tsvin:
#     	name = row[0]+'.json'
#     	boolFind = find(name, '/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/')
#     	if boolFind:
#     		print([row[0]])
#     		csvout.writerow([row[0]])

for file in os.listdir("/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/acousticbrainz-mediaeval-train/00/"):
    if file.endswith(".json"):
        filename = (os.path.join("/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/acousticbrainz-mediaeval-train/00/", file))
        print file
        with open(filename) as data_file:    
            data = json.load(data_file)
            average_loudness = data["lowlevel"]["average_loudness"]
            spectral_energy = data["lowlevel"]["spectral_energy"]["mean"]
            spectral_centroid = data["lowlevel"]["spectral_centroid"]["mean"]
            pitch_salience = data["lowlevel"]["pitch_salience"]["mean"]
            mfcc = data["lowlevel"]["mfcc"]["mean"]
            print mfcc

            new_json_file = {
                'average_loudness' : average_loudness,
                'spectral_energy' : spectral_energy,
                'spectral_centroid' : spectral_centroid,
                'pitch_salience' : pitch_salience,
                'mfcc' : mfcc
            }
            json_dump=json.dumps(new_json_file)
            print json_dump

            new_json_path = '/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/00_NEW/'+file

            with open(new_json_path, 'w') as outfile:
                json.dump(json_dump, outfile)

#pprint(data)

# boolFind = find('1a00a335-fead-46ec-8d4f-06e8341291ea.json', '/Users/Kharisnawan/OneDrive/Macbook White New/MMSR/project/')
# if boolFind:
# 	print(boolFind)