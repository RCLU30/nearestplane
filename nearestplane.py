from urllib.request import urlopen
# from math import acos, sin, cos, radians
import json
import math
import requests

EARTHRADIUS = 6353

def find_closest_plane(latitude, longitude):
    """
    Input: longitude (y) and latitude(x)
    Ouput: information on the nearest plane based on input long/lat coord
    """
    print(f"Input:\n >> latitude: {latitude}, longitude: {longitude}\n")
    #look for planes +/-1 degree of target coordinates
    baseurl = f"https://opensky-network.org/api/states/all?lamin={latitude-1}&lomin={longitude-1}&lamax={latitude+1}&lomax={longitude+1}"
    # r = requests.get(baseurl)
    listplanes = requests.get(baseurl).json()['states']
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
    print(f"Shortest distance is {shortest_distance}.")
    print(f"""
Geodesic distance: {shortest_distance}
Callsign: {nearestPlane[1]}
Lattitude and Longitude: {nearestPlane[6]}, {nearestPlane[5]}
Geometric Altitude: {nearestPlane[7]}
Country of origin: {nearestPlane[2]}
ICAO24 ID: {nearestPlane[0]}
    """)


# calculates geometric distance between input coordinates and plane coordinates
def geo_distance(x, y, planex, planey):
    # delta = acos(sin(latcoord)*sin(x) + cos(longcoord) * cos(y) * cos())
    return math.sqrt((planey-y)**2 + (planex-x)**2)


find_closest_plane(48.8584, 2.2945)
