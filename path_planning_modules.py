

# Author DHAVAL PATEL
# Saturday 14th sept

#import sys
#sys.path.insert(0, "/home/dhaval/Documents")

 # sample
 #poly = [(6.501182,52.987571),(6.381873,52.883827),(6.337962,52.766821),(6.667519,52.76689),(6.810511,52.967688),(6.659516,52.976018),(6.639138,52.971046),(6.572554,52.967302),(6.549302,52.97091)]
    # Sample circular polygon and source+ destination for it :
#poly = [(5.648056,52.331062),(5.64816,52.329611),(5.648471,52.328172),(5.648984,52.326755),
#	(5.649698,52.32537),(5.650605,52.324029),(5.6517,52.322742),(5.652973,52.321518),
#	(5.654416,52.320366),(5.656017,52.319296),(5.657764,52.318315),(5.659644,52.317432),
#	(5.661642,52.316652),(5.663744,52.315982),(5.665933,52.315426),(5.668192,52.31499),
#	(5.670505,52.314676),(5.672853,52.314487),(5.67522,52.314423),(5.677587,52.314487),
#	(5.679935,52.314676),(5.682248,52.31499),(5.684507,52.315426),(5.686696,52.315982),
#	(5.688797,52.316652),(5.690796,52.317432),(5.692676,52.318315),(5.694423,52.319296),
#	(5.696024,52.320366),(5.697467,52.321518),(5.69874,52.322742),(5.699835,52.324029),
#	(5.700742,52.32537),(5.701456,52.326755),(5.701969,52.328172),(5.70228,52.329611),
#	(5.702384,52.331062),(5.702281,52.332512),(5.701973,52.333952),(5.701461,52.335369),
#	(5.700749,52.336754),(5.699843,52.338095),(5.698749,52.339383),(5.697476,52.340608),
#	(5.696034,52.34176),(5.694433,52.342831),(5.692686,52.343812),(5.690805,52.344696),
#	(5.688806,52.345476),(5.686704,52.346147),(5.684514,52.346703),(5.682253,52.347139),
#	(5.679939,52.347454),(5.677588,52.347643),(5.67522,52.347707),(5.672852,52.347643),
#	(5.670501,52.347454),(5.668187,52.347139),(5.665926,52.346703),(5.663736,52.346147),
#	(5.661634,52.345476),(5.659635,52.344696),(5.657754,52.343812),(5.656007,52.342831),
#	(5.654406,52.34176),(5.652964,52.340608),(5.651691,52.339383),(5.650597,52.338095),
#	(5.649691,52.336754),(5.648979,52.335369),(5.648467,52.333952),(5.648159,52.332512)]

#source = 5.680501,52.357454
#destination = 5.658401,52.305454
# Google Earth format to plot a point(6.501182,52.987571) on map: in search box type '6.501182E,52.987571N' by adding 'E' at the end of x, and 'N' at the end of y coordinate of point

# category classification
# useful : the function can be edited for making program compact while making sure it serves same purpose
# fundamental : the function may be changed only if the conceptual idea of algorithm is changed

from shapely.geometry import Point, Polygon, LineString, MultiPoint

def inpoly(x,y,poly):
    p1 = Point(x,y)
    Poly = Polygon(poly)
    return p1.within(Poly)
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
    dilated = line.buffer(0.0007,join_style = 2, cap_style = 3)
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
        
        
        
def make_line(diagonal):   ### k determines the amount of points you want on this line, more k, moke dots, more precision
    p1 = diagonal[0]   ## diagonal = ([x1,y1],[x2,y2])
    p2 = diagonal[1]
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    k = 1000
    if abs(dx)>= abs(dy):
        ds = int(abs(k*(dx)))
    else:
        ds = int(abs(k*(dy)))
    line = [diagonal[0]]
    #print ds
    for i in range(abs(int(ds))-1):
        line.append([line[len(line)-1][0] + (dx/ds),line[len(line)-1][1] + (dy/ds)])
    #line.append(diagonal[1])
    del line[0]
    del line[len(line)-1]
##    if len(line) >=5:
##            del line[len(line)-1]
    return line  # list of lists(pairs of x,y)

import matplotlib.pyplot as plt


def plot_polys(poly): # poly is list of polygons and a polygon is lis of (x,y) pairs
    plt.axis([-5,45,-5,45])
    for p in poly:
        x = []
        y = []
        for pl in p:
            x.append(pl[0])
            y.append(pl[1])
        x.append(p[0][0])
        y.append(p[0][1])
        plt.plot(tuple(x),tuple(y))
    plt.show()


def check_line_inside(line,poly):
    flag = False
    for i in range(len(line)-1):
        if inpoly(line[i][0],line[i][1],poly):
            flag = not flag
            return flag

    return flag



def find_visible_nodes(source,polygon):
    #Sample source to try as testing source = (6.667519, 52.99689) with respect to the polygon above
    visible_nodes = []
    for i in range(len(polygon)):
        if polygon[i] == source:
            continue
        else:

            line = make_line((source,polygon[i]))
            flag = check_line_inside(line,polygon)
            if flag == False:
                visible_nodes.append(polygon[i])
    return visible_nodes

def find_nearby_nodes(node,poly):
    # Category : Fundamental
    # Gives two nearby nodes (on polygon) to the node of interest on the polygon

    i = poly.index(node)  # node is tuple (x,y)
    if i == len(poly)-1:
        next_node = poly[0]
        previous_node = poly[i-1]
    elif i == 0:
        next_node = poly[i+1]
        previous_node = poly[len(poly)-1]
    else:
        next_node = poly[i+1]
        previous_node = poly[i-1]
    nearby_nodes = [previous_node,next_node]
    return nearby_nodes # of the two nearby nodes, node with smaller index than given node is considered previous node


def find_feasible_nodes(source,poly):
    # Category : Fundamental
    # Finds two points such that the nearby point of each of these two is a point on polygon not seen from source
    feasible_nodes = []
    visible_nodes = find_visible_nodes(source,poly)
    if len(visible_nodes) == 2:
        return visible_nodes

    for i in range(len(visible_nodes)):
        nearby_nodes = find_nearby_nodes(visible_nodes[i],poly)
        if not (nearby_nodes[0] in visible_nodes):
            feasible_nodes.append(visible_nodes[i])
        if not (nearby_nodes[1] in visible_nodes):
            feasible_nodes.append(visible_nodes[i])
    return feasible_nodes # always gives two feasible nodes as there are only two ultimate ways of going around an obstacle


def dist(p1,p2):
    from math import hypot
    dist = hypot((p1[0]-p2[0]),(p1[1]-p2[1]))
    return dist


def overcome_obstacle(source,destination,poly):

    #category : Important + Fundamental

    # finds a temporary optimum path in the form of list.
    # the path is found such that if there is an obstacle between source and destination then the
    # shortest path will be generated from S to D with way points on the obstacle edges
    # Sample destination point: destination = (6.947962,52.916821)
    # Sample source point: source = 6.347962,52.916821
    # sample obstacle poly
    # poly = [(6.501182,52.987571),(6.381873,52.883827),(6.337962,52.766821),(6.667519,52.76689),(6.810511,52.967688),(6.659516,52.976018),(6.639138,52.971046),(6.572554,52.967302),(6.549302,52.97091)]



## GPP source = 6.724628, 52.024598
## GPP destination = 6.930354, 52.26502
    Feasible_nodes = find_feasible_nodes(source,poly)
    visible_nodes = find_visible_nodes(source,poly)
    visible_nodes.append(source)
    path1 = [source,Feasible_nodes[0]]
    path2 = [source,Feasible_nodes[1]]
    if destination in Feasible_nodes:
        if Feasible_nodes[0] == destination:
            return path1
        if Feasible_nodes[1] == destination:
            return path2

    #taking path1 first
    #next_possible_nodes = find_nearby_nodes(path1[1],poly)
    line1 = make_line([destination,path1[len(path1)-1]])
    if not (check_line_inside(line1,poly)):
        path1.append(destination)
    else:
        next_possible_nodes = find_nearby_nodes(path1[len(path1)-1],poly)
        if not (next_possible_nodes[0] in visible_nodes):
            next_node = next_possible_nodes[0]
        else:
            next_node = next_possible_nodes[1]
        path1.append(next_node)
        visible_nodes.append(next_node)
        while path1[len(path1)-1] != destination:
            line = make_line([path1[len(path1)-1],destination])
            if not check_line_inside(line,poly):
                path1.append(destination)
                break
            else:
                next_possible_nodes = find_nearby_nodes(path1[len(path1)-1],poly)
                if not (next_possible_nodes[0] in path1):
                    next_node = next_possible_nodes[0]
                else:
                    next_node = next_possible_nodes[1]
                path1.append(next_node)


    line2 = make_line([destination,path2[len(path2)-1]])
    if not (check_line_inside(line2,poly)):
        path2.append(destination)
    else:
        next_possible_nodes = find_nearby_nodes(path2[len(path2)-1],poly)
        if not (next_possible_nodes[0] in visible_nodes):
            next_node = next_possible_nodes[0]
        else:
            next_node = next_possible_nodes[1]
        path2.append(next_node)
        visible_nodes.append(next_node)
        while path2[len(path2)-1] != destination:
            line = make_line([path2[len(path2)-1],destination])
            if not check_line_inside(line,poly):
                path2.append(destination)
                break
            else:
                next_possible_nodes = find_nearby_nodes(path2[len(path2)-1],poly)
                if not (next_possible_nodes[0] in path2):
                    next_node = next_possible_nodes[0]
                else:
                    next_node = next_possible_nodes[1]
                path2.append(next_node)

    d1 = 0
    d2 = 0
    for i in range(len(path1)-1):
        d1 = d1 + dist(path1[i],path1[i+1])
    for i in range(len(path2)-1):
        d2 = d2 + dist(path2[i],path2[i+1])
    if d1 >= d2:
        path = path2
        #print d1,d2, 'd1 selected'
    else:
        path = path1
        #print d1,d2, 'd2 selected'
    return path




def order_of_hit(source,destination,obstacles):

    if source == destination:
            return []
    l = make_line([source,destination])
    index = []
    for poly in obstacles:
        for point in l:
            if inpoly(point[0],point[1],poly):
                index.append(((l.index(point)),(obstacles.index(poly))))
                break
    if index == []:
        return []
    data = dict(index)
    k = []
    for p in index:
        k.append(p[0])

    k.sort()
    order = []
    for i in k:
        order.append(data[i])

    return order

