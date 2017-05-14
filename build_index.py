import json
from geodata import GEODATA

index = {}

with open('cleaned_with_terms.csv') as f:
  for line in f.readlines():

    line = line.strip().split('|')

    # Convert datetime
    date = line[0].split(' ')[0]
    city = line[1]
    state = line[2]
    location = city + ',' + state
    terms = line[7].split(';')

    if len(terms) == 0:
      continue

    try:
      geo = GEODATA[location]
    except:
      continue

    for term in terms:

      if term not in index:
        index[term] = []

      index[term].append({ 
        'date': date,
        'city': city, 
        'state': state,
        'geo': geo 
      })


output = open('term_location_index.json', 'w+')
output.write(json.dumps(index))
output.close()
