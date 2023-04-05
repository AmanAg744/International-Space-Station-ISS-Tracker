import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file  = open("iss.txt", "w")
file.write("There are currently" + str(result["number"]) + "astronauts on board the iss: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + "- on board" + "\n")
g = geocoder.ip('me')
file.write("\n your current lat/long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")


#set up world map in turtle module
screen = turtle.Screen()
screen.setup(1250, 700)
screen.setworldcoordinates(-180,-90,180,90)


#load the world map image
screen.bgpic("world map.gif")
screen.register_shape("iss icon.gif")
iss = turtle.Turtle()
iss.shape("iss icon.gif")
iss.setheading(45)
iss.penup()


while True:
    #load current status of iss in real time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #extract iss location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    #output lon and lat
    lat = float(lat)
    lon = float(lon)
    print("\nLAtitude : " + str(lat))
    print("\nLongitude : " + str(lon))
     
    #update location on map
    iss.goto(lon,lat)

    #refresh each 5 sec
    time.sleep(5)