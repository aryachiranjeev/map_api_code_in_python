import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAv83lNDUwQ7C9McltKYlvpnEq4QZYSOZ4')


now = datetime.now()
directions_result = gmaps.directions("18.997739, 72.841280",
                                     "18.880253, 72.945137",
                                      waypoints=["Barossa Valley, SA",
                                                  "Clare, SA",
                                                  "Connawarra, SA",
												  "McLaren Vale, SA"],
                                     optimize_waypoints=True,
                                     mode="transit",
                                     transit_mode="bus",
                                     departure_time=now,
                                    )

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])