#Import important libraries
import gmplot
import numpy as np
# generate 700 random lats and lons
latitude = (np.random.random_sample(size = 700) - 0.5) * 180
longitude = (np.random.random_sample(size = 700) - 0.5) * 360
# declare the center of the map, and how much we want the map zoomed in
gmap = gmplot.GoogleMapPlotter(0, 0, 2)
# plot heatmap
gmap.heatmap(latitude, longitude)
gmap.scatter(latitude, longitude, c='r', marker=True)
#Your Google_API_Key#
#gmap.apikey = " Your_Google_API_Key "
# save it to html
gmap.draw("./map.html")
