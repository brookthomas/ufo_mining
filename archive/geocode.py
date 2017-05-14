import requests
import json
import time

REQUESTS_PER_SECOND = 3
MAPS_API_KEY = 'AIzaSyD1BlM3rzNSw1qt-M3xZu3-nhqX9yVXUXY'
URL_TEMPLATE = "https://maps.googleapis.com/maps/api/geocode/json?address={}&components=country:US&key=" + MAPS_API_KEY

outfile = open('geocode_output.txt','w+')
counter = 0

# Open locations.txt
with open('locations_remaining.txt') as f:
    for loc in f.readlines():
        loc = loc.strip()

        url = URL_TEMPLATE.format(loc)

        response = requests.get(url)

        # Exit if we don't get a good response code (likely over rate limit)
        if response.status_code != 200:
            print('Response {}. EXITING.'.format(response.status_code))
            quit()

        parsed = json.loads(response.text)

        if parsed['status'] != 'OK':
            print('Status {} for Location {}. SKIPPING'.format(parsed['status'], loc))
            continue

        lat = parsed['results'][0]['geometry']['location']['lat']
        lng = parsed['results'][0]['geometry']['location']['lng']

        outfile.write('{};{};{}\n'.format(loc,lat,lng))

        counter += 1
        if counter % 10 == 0:
            print(counter)

        time.sleep( 1 / REQUESTS_PER_SECOND )