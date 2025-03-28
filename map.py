import folium 
import pandas

map=folium.Map(location=[28.7041, 77.1025],zoom_start=11) #creating an object called 'map' and passing the latitudes(range from -90 to 90) and longitudes(range from -180 to 180) in form of a list
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

fgm=folium.FeatureGroup(name="Metro stations")#creating a feature group to make it more organised

#for loop to iterate through the data and add markers
for lt,lo,st,lin in zip(lat,lon,stat,line):
    fgm.add_child(folium.Marker(location=[lt,lo], popup=str(st),icon=folium.Icon(color=color_produce(lin)))) #marker allows you to add popups. 

fgp=folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read() , 
style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] <100000000
else 'orange' if 10000000<x['properties']['POP2005']<200000000 else 'red'}) ) #utf-8-sig makes sure the file is read correctly, even if it has a special marker at the start. 

map.add_child(fgm)
map.add_child(fgp)#calling the feature group
map.add_child(folium.LayerControl())
map.save("MAP1.html") #saves 'map' in a html format
