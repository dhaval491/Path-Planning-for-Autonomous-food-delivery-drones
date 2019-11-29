# Extracts the polygon coordinates (no_fly_zones) for input to GPP
# Output is lists of no_flyzones in format of list lat-long pairs

import pickle
from shapely.geometry import Polygon,Point
from shapely.ops import cascaded_union
from shapely.ops import unary_union


def inpoly(x,y,poly):
	p = Point(x,y)
	Poly = Polygon(poly)
	return p.within(Poly)



import xml.etree.ElementTree as ET
# importing kml file and finding all texts contents as object under attributes 'coordinates'
filePath = r'./src/Drone_No_Fly_Zones_nl.kml'
tree = ET.parse(filePath)
poly = tree.findall('.//{http://www.opengis.net/kml/2.2}coordinates')
import re
poly_text = []
# extract text of every object into a list
for i in range(len(poly)):
	poly_text.append(poly[i].text)


# removing spaces from every text object and every object will be in form of [x1,y1,0,x2,y2,0 ... Xn,Yn,0]
poly_float_text = []
for i in range(len(poly_text)):
	poly_float_text.append(re.findall(r"[-+]?\d*\.\d+|\d+",poly_text[i]))
# removing zeros and sorting  x and y into format of [(x1,y1),(x2,y2)....(Xn,Yn)]
polygons = []
for k in poly_float_text:
    b = []
    for c in k:
        b.append(float(c))
    a = []
    for x in b:
        if x == 0.0:
            continue
        else:
            a.append(x)
    k = []
    for i in range(0,len(a)-2,2):
        k.append((a[i],a[i+1]))
    polygons.append(k)
# after running this module we get lists of polygons areas in variable name 'polygons'
# etherpad_for merging inbetween modules
# removing empty polygons
Filtered_polygons = []
for poly in polygons:
        if poly == []:
                continue
        else:
                Filtered_polygons.append(poly)
polygons = Filtered_polygons


# removing duplicate regions
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

p = Remove(polygons)
polygons = p
# polyogns is list of all polygons that are intersecting or completely submerged
