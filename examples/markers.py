# -*- coding: utf-8 -*-
'''Test of Folium basic markers'''

import folium

#Simple Markers with Stamen Terrain
map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12,
                   tiles='Stamen Terrain')
map_1.simple_marker([45.3288, -121.6625], popup='Mt. Hood Meadows')
map_1.simple_marker([45.3311, -121.7113], popup='Timberline Lodge')
map_1.create_map(path='mthood.html')

#Circle Markers with Stamen Toner
map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',
                   zoom_start=13)
map_2.simple_marker(location=[45.5244, -122.6699], popup='The Waterfront')
map_2.circle_marker(location=[45.5215, -122.6261], radius=500,
                    popup='Laurelhurst Park', line_color='#3186cc',
                    fill_color='#3186cc')
map_2.create_map(path='portland.html')

#Lat/Lng popovers
map_3 = folium.Map(location=[46.1991, -122.1889], tiles='Stamen Terrain',
                   zoom_start=13)
map_3.lat_lng_popover()
map_3.create_map(path='sthelens.html')

#Click for marker
map_4 = folium.Map(location=[46.8527, -121.7649], tiles='Stamen Terrain',
                   zoom_start=13)
map_4.simple_marker(location=[46.8354, -121.7325], popup='Camp Muir')
map_4.click_for_marker(popup='Waypoint')
map_4.create_map(path='mtrainier.html')
