## test
##import sys
##sys.path.insert(0, ".")
from src.path_planning_modules import*
from src.Polygons_from_kml import*
from src.scrubbing import*

##source = (6.33722222,52.05222222)
##destination = 6.96333333,52.30750000
####

source = 6.11444444,52.12305556
destination = 6.50111111,52.38416667

##source = 5.49333333,52.38583333
##destination = 6.24027778,52.52472222




##ts = source
##td = destination
##tp = []
##p = [destination]
##while not order == []:
##    order = order_of_hit(source,td,Ob)
##    if order == []:
##        p.append(source)
##        break
##    tp = overcome_obstacle(source,td,Ob[order[len(order)-1]])
##    print len(tp)
####    if len(tp) == 3:
####        if len(Ob) == 1:
####            order = []
####        del Ob[len(Ob)-1]
####
##    next_node = tp[len(tp)-2]
##    p.append(next_node)
##
##    td = next_node

## Checking if the destination is in no_fly_zone or not


def check_destination_validity(destination,refined_polygons):
    flag = True
    for pl in refined_polygons:
        if inpoly(destination[0],destination[1],pl):
            print("Destination is in a no_fly_zone")
            flag = not flag
    return flag

def compute_gpp(source, destination, refined_polygons = refined_polygons):

    obstacles = []

    print(source)
    print(destination)

    l = make_line([source,destination])

    for p in refined_polygons:
        if check_line_inside(l,p):
            obstacles.append(p)

    index = []
    for i in range(len(obstacles)):
        index.append([i])


    Ob = merged_regions(obstacles,index)




    order = order_of_hit(source,destination,Ob)

    ts = source
    td = destination
    tp = [destination]
    p = [source]
    Order = order_of_hit(source,destination,Ob)
    if Order == []:
        p.append(destination)
        return p
    else:
        while not Order == []: ## check for New Ob at every new ts
            Order = order_of_hit(ts,destination,Ob)
            if Order == []:
                p.append(destination)
                break
            tp = [destination]
            td = destination
            order = order_of_hit(ts,td,Ob)
            while not order == []:
                order = order_of_hit(ts,td,Ob)
                if order == []:
                    tp.append(ts)
                    break
                tps = overcome_obstacle(ts,td,Ob[order[len(order)-1]])
                print(len(tps))
            ##    if len(tp) == 3:
            ##        if len(Ob) == 1:
            ##            order = []
            ##        del Ob[len(Ob)-1]
            ##
        ##        if len(tps) == 2:
        ##            if not order == []
        ##            td = tps[len(tps)-1]
        ##            tp.append(ts)
        ##            break
                td = tps[len(tps)-2]
                if td == ts:
                    tp.append(ts)
                    break
                tp.append(td)
            ts = tp[len(tp)-2]
            if ts == destination:
                p.append(destination)
                break
            p.append(ts)
        #print(p)
    return p


if __name__ == '__main__':
    compute_gpp(source,destination)



