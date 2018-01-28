import json


infile = open('averaged_genres.json', 'r')
f = json.load(infile)

for key in f.keys():
	f[key]['tempo'] = f[key]['tempo'] / float(250)

with open('proper_avg_gen.json', 'w') as outfile:
	json.dump(f, outfile, indent=4)