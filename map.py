import folium 
import pandas

map=folium.Map(location=[12,77],zoom_start=6) #creating an object called 'map' and passing the latitudes(range from -90 to 90) and longitudes(range from -180 to 180) in form of a list
data=pandas.read_csv("DELHI_METRO_DATA.csv")

def color_produce(li):
    if li== "Yellow Line":
        return 'lightgreen'
    elif li== "Red Line":
        return 'red'
    elif li=="Violet Line":
        return 'purple'
    elif li=="Blue Line":
        return 'blue'
    elif li=="Green Line":
        return 'green'
    elif li=="Pink Line":
        return 'pink'
    elif li=="Orange Line":
        return 'orange'
    elif li=="Magenta Line":
        return 'darkpurple'
    elif li=="Grey Line":
        return 'gray'
    else:
        return 'beige'
    
#making several lists extracting the colum values in a form of a list
lat=list(data["Latitude"]) 
lon=list(data["Longitude"])
stat=list(data["Station"])
line=list(data["Line"])

fg=folium.FeatureGroup(name="My map")#creating a feature group to make it more organised

#for loop to iterate through the data and add markers
for lt,lo,st,lin in zip(lat,lon,stat,line):
    fg.add_child(folium.Marker(location=[lt,lo], popup=str(st),icon=folium.Icon(color=color_produce(lin)))) #marker allows you to add popups.
    
map.add_child(fg)  #calling the feature group
map.save("MAP1.html") #saves 'map' in a html format
