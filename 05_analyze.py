from haversine import haversine
from scipy import stats
import datetime
import pickle

MINIMUM_SIGHTINGS = 30
SECONDS_IN_DAY = 60 * 60 * 24


index = pickle.load(open('term_position_index.pickle','rb'))

for term, sightings in index.items():

    if len(sightings) < MINIMUM_SIGHTINGS:
        continue

    sightings.sort( key = lambda s: s['date'] )

    # Establish first sighting
    first = sightings[0]

    # For all subsequence sightings, get the distance and time deltas
    distance_delta = [haversine(first['geo'], s['geo']) for s in sightings]
    time_delta = [int((s['date'] - first['date']).total_seconds() / SECONDS_IN_DAY) for s in sightings]

    # Find correalation coefficient from these arrays and store result
    ccf = stats.pearsonr(time_delta, distance_delta)

    print("{},{},{},{}".format(term, len(sightings), round(ccf[0],3), round(ccf[1],3)))