from haversine import haversine
from scipy import stats
import datetime
import json

MINIMUM_SIGHTINGS = 30
SECONDS_IN_DAY = 60 * 60 * 24

def str_to_date( date ):
    date = date.split('/')
    date = [i for i in map(int, date)]
    date[2]+= 1900
    try:
        return datetime.date(date[2],date[0],date[1])
    except:
        return datetime.date(date[2],date[0],28)



with open('term_location_index.json') as f:
    index = json.loads(f.read())

for term, sightings in index.items():

    if len(sightings) < MINIMUM_SIGHTINGS:
        continue

    # Convert dates to python date objects and sort
    for s in sightings:
        s['date'] = str_to_date(s['date'])

    sightings.sort( key = lambda s: s['date'] )

    # Establish first sighting
    first = sightings[0]

    # For all subsequence sightings, get the distance and time deltas
    distance_delta = [haversine(first['geo'], s['geo']) for s in sightings]
    time_delta = [int((s['date'] - first['date']).total_seconds() / SECONDS_IN_DAY) for s in sightings]

    # Find correalation coefficient from these arrays and store result
    ccf = stats.pearsonr(time_delta, distance_delta)

    print("{},{},{},{}".format(term, len(sightings), round(ccf[0],3), round(ccf[1],3)))


print(index['greenish'])
print(index['orangeish'])