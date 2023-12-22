
International Space Station (ISS) Tracker
Overview
This Python project utilizes various APIs and libraries to track the real-time location of the International Space Station (ISS) and provides information about the astronauts on board. The project includes the use of the Open Notify API for astronaut data and ISS location, the Turtle module for creating a simple graphical user interface with a world map, and the Geocoder library to fetch the user's current latitude and longitude based on their IP address.

Features
Retrieves and displays the current number of astronauts on board the ISS along with their names.
Fetches the user's current latitude and longitude using the Geocoder library.
Displays the real-time location of the ISS on a world map using the Turtle module.
Updates the ISS location every 5 seconds to reflect its movement.
Getting Started
Clone the repository to your local machine.
Install the required Python libraries: turtle, urllib, json, time, webbrowser, and geocoder.
Run the Python script to generate the "iss.txt" file with astronaut information and open it in the default web browser.
The Turtle graphics window will open, displaying the world map with an icon representing the ISS.
The program will continuously update the ISS location on the map every 5 seconds.
Project Structure
iss.py: Python script containing the main code for fetching ISS and astronaut data, creating the "iss.txt" file, and displaying the ISS on the world map.
world map.gif: Image file used as the background for the Turtle graphics window.
iss icon.gif: Image file used as the icon representing the ISS on the world map.
Dependencies
Python 3.x
Turtle module
Geocoder library
Acknowledgments
Open Notify API for providing real-time ISS data.
Geocoder library for retrieving user location based on IP address.
Feel free to contribute, report issues, or suggest improvements!
