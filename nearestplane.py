from math import acos, sin, cos, radians, sqrt
import requests

EARTHRADIUS = 6353 # in kilometers

def find_closest_plane(latitude, longitude):
    """
    Input: longitude (y) and latitude(x)
    Ouput: information on the nearest plane based on input long/lat coord
    """
    print(f">> Input coordinates:\n>> Latitude: {latitude}\n>> Longitude: {longitude}\n")

    lamin = latitude
    lomin = longitude
    lamax = latitude
    lomax = longitude

    while True:
        #look for planes +/-1 degree of target coordinates
        # perform search and expand range of search until planes are found
        lamin -= 1
        lomin -= 1
        lamax += 1
        lomax += 1
        baseurl = f"https://opensky-network.org/api/states/all?lamin={lamin}&lomin={lomin}&lamax={lamax}&lomax={lomax}"
        # r = requests.get(baseurl)
        listplanes = requests.get(baseurl).json()['states']
        if listplanes:
            break

    distances = []
    shortest_distance = 0
    shortest_index = ''

    if listplanes is None:
        print("No planes found")
    else:
        for plane in listplanes:
            distances.append(geo_distance(latitude, longitude, plane[6], plane[5]))

    shortest_distance = (min(distances))
    shortest_index = distances.index(shortest_distance)
    nearestPlane = listplanes[shortest_index]
    print(f""">> Geodesic distance(approximate): {shortest_distance} meters
>> Callsign: {nearestPlane[1]}
>> Lattitude and Longitude: {nearestPlane[6]}, {nearestPlane[5]}
>> Geometric Altitude: {nearestPlane[7]}
>> Country of origin: {nearestPlane[2]}
>> ICAO24 ID: {nearestPlane[0]}""")

# distance coordinates using euclidian calculation
# def geo_distance(x, y, planex, planey):
#     return sqrt((planey-y)**2 + (planex-x)**2)

# distance coordinates using geodesic calculation
def geo_distance(x, y, planex, planey):
    xrad = radians(x)
    yrad = radians(y)
    planexrad = radians(planex)
    planeyrad = radians(planey)
    return EARTHRADIUS * acos(sin(xrad) 
            * sin(yrad) 
            + cos(xrad) 
            * sin(yrad) 
            * cos(abs(planexrad - planeyrad)))

# eiffel tower
find_closest_plane(48.8584, 2.2945)

# jfk aiport
# find_closest_plane(40.6413, -73.7781

#random location in canada
# find_closest_plane(48.6413, -73.7781)
