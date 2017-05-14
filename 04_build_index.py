import pickle
from geodata import GEODATA

index = {}

sightings = pickle.load(open('sightings_terms.pickle','rb'))

for s in sightings:

  # Convert datetime
  date = s[0]
  city = s[1]
  state = s[2]
  location = city + ',' + state
  terms = s[3]

  if len(terms) == 0:
    continue

  try:
    geo = GEODATA[location]
  except:
    print(location)
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


file = open('term_position_index.pickle','wb+')
pickle.dump(index, file)
file.close()
