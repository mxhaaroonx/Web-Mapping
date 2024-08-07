import folium 
map=folium.Map(location=[12,77],zoom_start=6) #creating an object called 'map' and passing the latitudes(range from -90 to 90) and longitudes(range from -180 to 180) in form of a list
map.add_child(folium.Marker(location=[12,77], popup="Home :)",icon=folium.Icon(color="red"))) #marker allows you to add popups 
map.save("MAP1.html") #saves 'map' in a html format
