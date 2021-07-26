
# Author - DHAVAL PATEL
#----------------------------------------Scrubbing-----------------------------#

import pickle
# removing polygons that are completely inside any other polygon
pickle_in = open("src/refined_polygons.pickle","rb")
refined_polygons = pickle.load(pickle_in)
##Intersected_poly = pickle.load(pickle_in)
##I_p = Remove(Intersected_poly)
##refined_polygons = []
##for poly in polygons: #polygons is the output of a kml/airmap file, the regions in form of list
##	if poly in I_p:
###		print 'poly skipped'
##		continue
##	else:
##		refined_polygons.append(poly)

##Overlapping_poly = []
##for i in range(0,len(refined_polygons)/10):
##        test_poly = refined_polygons[i]
##        for poly in refined_polygons:
##                if poly == test_poly or poly == []:
##                        continue
##                else:
##                        intersection_points = []
##                        for p in poly:
##                                if inpoly(p[0],p[1],test_poly):
##                                        intersection_points.append(p)
##                                        #print 'interesection points detected'
##                        if intersection_points == poly:
##                                Intersected_poly.append(poly)
##                                print i
##
## took 45 mins to run and store intersected_poly as a pickle obbject




from shapely.geometry import Polygon,Point, LineString, MultiPoint
from shapely.ops import cascaded_union
from shapely.ops import unary_union

def make_hull(p):
    R = p
    R.append(p[0])
    line  = LineString(R)
    dilated = MultiPoint(p).convex_hull
    x, y = dilated.exterior.coords.xy
    merged_sample = []
    for i in range(len(x)-1):
        merged_sample.append((x[i],y[i]))
    return merged_sample

def dilate_poly(r):
    R=r
    R.append(R[0])
    line = LineString(R)
    dilated = line.buffer(0.007,join_style = 2, cap_style = 3)
    x, y = dilated.exterior.coords.xy
    merged_sample = []
    for i in range(len(x)-1):
        merged_sample.append((x[i],y[i]))
    return merged_sample

def make_rect(p):
    R = p
    R.append(p[0])
    line  = LineString(R)
    dilated = MultiPoint(p).minimum_rotated_rectangle
    x, y = dilated.exterior.coords.xy
    merged_sample = []
    for i in range(len(x)-1):
        merged_sample.append((x[i],y[i]))
    return merged_sample

def inpoly(x,y,poly):
    p1 = Point(x,y)
    Poly = Polygon(poly)
    return p1.within(Poly)


# function to find unions fo two polys

def cascade_polygons(poly1,poly2):
    polygon1 = Polygon(poly1)
    polygon2 = Polygon(poly2)
    polygons = [polygon1, polygon2]
    u = cascaded_union(polygons)
    x, y = u.exterior.coords.xy
    merged_sample = []
    for i in range(len(x)-1):
        merged_sample.append((x[i],y[i]))
    return merged_sample

# check if two polygons have same elements i.e. [1,2,3] is same as [3,1,2]
def check_equality(poly1,poly2):
    for p in poly1:
        if not p in poly2:
            return False
    for p in poly2:
        if not p in poly1:
            return False
    return True

# for testing purpose, finding first 10 polys that are intersecting each other
##Overlapping_poly = []
##for i in range(0,len(refined_polygons)/70): #for testing 70 is taken as fator and length of the output is limited to 2 objects
##        test_poly = refined_polygons[i]
##        if len(Overlapping_poly) > 9:
##            break
##        for poly in refined_polygons:
##                if len(Overlapping_poly) > 9:
##                    break
##                if poly == test_poly:
##                        continue
##                else:
##                        for p in poly:
##                                if inpoly(p[0],p[1],test_poly):
##                                    if poly not in Overlapping_poly:
##                                        Overlapping_poly.append(poly)
##                                    if test_poly not in Overlapping_poly:
##                                        Overlapping_poly.append(test_poly)
##
##testing : formating values for next algorithm
##F = True
##while F:
##    next_poly = []
##    prev_poly = x
##    flag  = True
##    inters = [1]
##    itr = 0
##    F  = not F

# algorithm implementation for finding union of all intersecting multiple polygons

## while flag:  # debugging left
##     if 1 in inters:
##         inters = []
##         flag = True
##         itr = itr + 1
##         print itr, ' ', len(prev_poly)
##         for i in range(len(prev_poly)):
##             test_poly = prev_poly[i]
##             for j in range(len(prev_poly)):
##                 poly = prev_poly[j]
##                 if poly == test_poly:
##                     continue
##                 else:
##                     for p in poly:
##                         if inpoly(p[0],p[1],test_poly):
##
##                             merged_poly = cascade_polygons(poly,test_poly)
##                             if merged_poly not in next_poly:
##                                 flag1 = True
##                                 next_poly.append(merged_poly)
##                             break
##                         else:
##                             flag1 =False
##                 if flag1:
##                     inters.append(1)
##                 else:
##                     inters.append(0)
##         prev_poly = next_poly
##         next_poly = []
##     else:
##         flag = False
##
from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from shapely.geometry import LineString
##poly0 = [(29,17),(35,18),(39,9),(31,8)]
##poly1 = [(18,10),(20,16),(24,15),(26,10)]
##poly2 = [(21,3),(19,9),(26,12),(29,6)]
##poly3 = [(2,15),(2,18),(5,18),(5,15)]
##poly4 = [(25,18),(29,19),(31,16),(26,15)]
##poly5 = [(26,4),(27,9),(33,11),(34,4)]
##poly6 = [(22,13),(23,17),(26,17.5),(27,14)]
##poly7 = [(14,6),(15,13),(22,11),(23,6)]
##poly8 = [(3,13),(3,17),(7,17),(7,13)]
##poly = [poly0,poly1,poly2,poly3,poly4,poly5,poly6,poly7,poly8]
##
### plotting polygons on a graph
##






def plot_polys(poly,line,axis): # poly is list of polygons and a polygon is lis of (x,y) pairs
    plt.axis(axis) ## Please make sure to include proper axis values
    for p in poly:
        x = []
        y = []
        for pl in p:
            x.append(pl[0])
            y.append(pl[1])
        x.append(p[0][0])
        y.append(p[0][1])

        plt.plot(tuple(x),tuple(y))
    x = []
    y =[]
    if not line == []:
        for point in line:
            x.append(point[0])
            y.append(point[1])
        plt.plot(tuple(x),tuple(y))
    plt.show()


def union(poly1,poly2): # finding union of lists of indext poly1 = [1,2,3,4,5] and poly2 = [3,4,5,6,7]
    set1 = set(poly1)
    set2 = set(poly2)
    return list(set1.union(set2)) # output = [1,2,3,4,5,6,7]


def intersection(poly1,poly2): # finding intersection of lists of indext poly1 = [1,2,3,4,5] and poly2 = [3,4,5,6,7]
    set1 = set(poly1)
    set2 = set(poly2)
    return list(set1.intersection(set2)) # output = [3,4,5]

# function to find union of multiple polyogns

# polys is main set of polygons and index is list of indices of polygons whose union is to be find out
# example index = [1,6,8] will give union of polygons with index 1,6,8

def union_polys(polys,index): # polys list of polygons (note that two adjectent polygons(indices) must be intersecting)
    if len(index) == 1:
        u = polys[index[0]]
    else:
        prev_union = polys[index[0]]
        for i in range(1,len(index)):
#            print i
            prev_union = cascade_polygons(prev_union,polys[index[i]])
        u = prev_union
    return u



# Check if two polys intersect

def check_intersection(poly1,poly2):
    polygon1 = Polygon(poly1)
    polygon2 = Polygon(poly2)
    P = polygon1.intersects(polygon2)
    return P




## Function to sort the indices such that union of multiple polygons can be obtained
## output of this function is list of indices that is used as one of input(index) for funtion named 'union_polys'
## The sorting is done such that every adjecent pair of polygons is intersecting
## poly is list of main polygons and index is list of indices that are not sorted in such a way that pair of any two
## adjecent polys according to indices in index is not intersecting
## index for input must be such that the polygons of this index forms intersecting chains irrespective of order of the indices in list

def sort_index(poly,index):
    if len(index)<2:
        return index
    else:
        P = []
        MI = [index[0]]
        RI = list(set(index).difference(set(MI)))
    #    print RI, MI
        TP = []
        while not RI == []:
            for i in range(len(RI)):
                P = union_polys(poly,MI)
                TP = poly[RI[i]]
                if check_intersection(P,TP):
                    MI.append(RI[i])
                    RI = list(set(RI).difference(set(MI)))
    #                print RI, MI, i
                    break
    #            else:
    #                print 'skipped'
        return MI



#index = [[0],[1],[2],[3],[4],[5],[6],[7],[8]]



## function to find is the given set is subset of any set in the given list of sets
## Next poly is list of sets
## u is a test set to check if it is subset of any sets in Next_poly

def check_subset_in_list(su,Next_poly):
    flag  =  False
    su = set(su)
    for u in Next_poly:
        if set(u) == su:
            continue
        else:
            if su.issubset(set(u)):
                return not flag

    return flag

def remove_subsets(Next_poly):
    NP_set = set(map(tuple,Next_poly))
    NP_filtered = map(list,NP_set)
    NP = []
    for p in NP_filtered:
        #print Next_poly.index(p)
        if check_subset_in_list(p,NP_filtered):
            continue
        else:
            NP.append(p)
    return NP



## Algorithm to find union of multiple polygon
## initialization


def merged_regions(poly,index):
    # poly is list of polygons
    # index is the index of polygons in poly list of a single element list

    Next_poly = []
    Prev_poly = index

    P = []
    P_index = []

    TP_inters = []
    Main_inters = [1]

    TP = []
    TP_index = []

    while 1 in Main_inters:
        Main_inters = []
        for i in range(len(Prev_poly)):
            P_index = Prev_poly[i]
            P = union_polys(poly,sort_index(poly,P_index))
            TP_inters = []
            for j in range(len(Prev_poly)):
                TP_index = Prev_poly[j]
                if TP_index == P_index:
                    TP_inters.append(0)
                    continue
                else:
                    TP = union_polys(poly,sort_index(poly,TP_index))
                    if check_intersection(P,TP):
                        su = sort_index(poly,union(TP_index,P_index))
                        #TP_inters.append(1)
                        if not(check_subset_in_list(su,Next_poly)):
                           Next_poly.append(su)
                           ##print 'appended' , Next_poly
                           TP_inters.append(1)
                        else:
                           TP_inters.append(0)
                    else:
                        TP_inters.append(0)
            Next_poly = remove_subsets(Next_poly)
            ##print TP_inters
            if 1 in TP_inters:
                Main_inters.append(1)
            if not (1 in TP_inters):
                Main_inters.append(0)
                Next_poly.append(sort_index(poly,P_index))
        Prev_poly = remove_subsets(Next_poly)
        Next_poly = []

    no_fly_zones = []
    for p in Prev_poly:
        U = union_polys(poly,p)
        no_fly_zones.append(U)
    nfz = []
    for i in no_fly_zones:
        nfz.append(make_hull(i))
    return nfz



##poly0 = [(18,15),(19,18),(22,18),(23,16)]
##poly2 = [(15.5,12),(16,17),(21,16),(22,12)]
##poly4 = [(17,11),(24,18),(26,14),(22,9)]
##poly5 = [(36,17),(37,14),(34,12),(32,14)]
##poly7 = [(34,16),(40,16),(41,12),(37,13.5)]
##poly6 = [(37,9),(39,15),(42,14),(41,8)]
##poly1 = [(38,6),(32,7),(33,14),(39,10)]
##poly = [poly0,poly1,poly2,poly3,poly4,poly5,poly6,poly7,poly8]
##
##
##Merged_poly_index = merged_regions(poly,index)
##no_fly_zones = []
##for p in Merged_poly_index:
##    U = union_polys(poly,p)
##    no_fly_zones.append(U)

##poly = [poly0,poly1,poly2,poly3,poly4,poly5,poly6,poly7,poly8]
##for p in no_fly_zones:
##    poly.append(p)
##
##plot_polys(no_fly_zones)








##
##
##
##def merged_regions(refined_poly,index):
##    # poly is list of polygons
##    # index is the index of polygons in poly
##    poly = refined_poly
##    Next_poly = []
##    Prev_poly = index
##
##    P = []
##    P_index = []
##
##    TP_inters = []
##    Main_inters = [1]
##
##    TP = []
##    TP_index = []
##
##    while 1 in Main_inters:
##        Main_inters = []
##        for i in range(len(Prev_poly)):
##            P_index = Prev_poly[i]
##            P = union_polys(poly,sort_index(poly,P_index))
##            TP_inters = []
##            for j in range(len(Prev_poly)):
##                TP_index = Prev_poly[j]
##                if TP_index == P_index:
##                    TP_inters.append(0)
##                    continue
##                else:
##                    TP = union_polys(poly,sort_index(poly,TP_index))
##                    if check_intersection(P,TP):
##                        su = sort_index(poly,union(TP_index,P_index))
##                        #TP_inters.append(1)
##                        if not(check_subset_in_list(su,Next_poly)):
##                           Next_poly.append(su)
##                           ##print 'appended' , Next_poly
##                           TP_inters.append(1)
##                        else:
##                           TP_inters.append(0)
##                    else:
##                        TP_inters.append(0)
##            Next_poly = remove_subsets(Next_poly)
##            ##print TP_inters
##            if 1 in TP_inters:
##                Main_inters.append(1)
##            if not (1 in TP_inters):
##                Main_inters.append(0)
##                Next_poly.append(sort_index(poly,P_index))
##        Prev_poly = remove_subsets(Next_poly)
##        Next_poly = []
##
##        no_fly_zones = []
##        for p in Prev_poly:
##            U = union_polys(poly,p)
##            no_fly_zones.append(U)
##        poly = no_fly_zones
##
##
##    return no_fly_zones
##
