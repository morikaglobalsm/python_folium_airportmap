import folium
import pandas

data = pandas.read_csv("airports.csv")

lon = data["longitude_deg"]
lat = data["latitude_deg"]
airportname = data["name"]
location = data["iso_country"]
airportsize = data["type"]

def icon_producer(airporttype):
    if airporttype == "large_airport":
        return "red"
    elif airporttype == "closed":
        return "black"
    else:
        return "blue"


# Initiate map object (lat, lon)
m = folium.Map(location=(30.583332, 114.283333), zoom_start=5, tiles="Stamen Terrain")

# tooltip
tooltip = "Click for Airport Name"

fg = folium.FeatureGroup(name = "China Airport Map")

# Create markers for China based airports from the csv file
for ln, lt, name, country, size in zip(lon, lat, airportname, location, airportsize):
    if country == "CN" or "JP":
        fg.add_child(folium.Marker(
            location = [lt, ln],
            popup = "<strong>{}</strong>".format(name),
            icon = folium.Icon(color=icon_producer(size),
            icon="plane"),
            tooltip = tooltip
        ))

m.add_child(fg)

m.save("map.html")