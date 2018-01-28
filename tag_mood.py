import json, codecs, csv

with open('tag_weights.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    tot = {'danceability': 0, 'loudness': 0, 'liveness': 0, 'energy': 0, 'valence': 0, 'tempo': 0, 'instrumentalness': 0, 'acousticness': 0}
    for row in spamreader:
    	if row[0] == 'tag':
    		continue
    	tot['danceability'] += float(row[1])
    	tot['loudness'] += float(row[2])
    	tot['liveness'] += float(row[3])
    	tot['energy'] += float(row[4])
    	tot['valence'] += float(row[5])
    	tot['tempo'] += float(row[6])
    	tot['instrumentalness'] += float(row[7])
    	tot['acousticness'] += float(row[8])
    print(tot)