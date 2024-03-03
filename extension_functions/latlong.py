import googlemaps

api_key = 'AIzaSyDNgl2UOlCrczRmcmIi8zJRNgYbaRx6paY'
gmaps = googlemaps.Client(key=api_key)
res = gmaps.geocode('Atherstone')
print(res)