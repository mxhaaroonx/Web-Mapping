import folium 
import pandas

map=folium.Map(location=[12,77],zoom_start=6) #creating an object called 'map' and passing the latitudes(range from -90 to 90) and longitudes(range from -180 to 180) in form of a list
data=pandas.read_csv("DELHI_METRO_DATA.csv")

lat=list(data["Latitude"])
lon=list(data["Longitude"])
stat=list(data["Station"])

fg=folium.FeatureGroup(name="My map")#creating a feature group to make it more organised
for lt,lo,st in zip(lat,lon,stat):
    fg.add_child(folium.Marker(location=[lt,lo], popup=str(st),icon=folium.Icon(color="red"))) #marker allows you to add popups.
    
map.add_child(fg)
map.save("MAP1.html") #saves 'map' in a html format
