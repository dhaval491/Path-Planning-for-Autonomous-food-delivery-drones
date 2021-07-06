# Food Delivery drone global-path-planning between delivery destination and the current location of the drone
**Notable Tasks**
**-> Parsing data from "No - Fly Zones" Map file that is in .kml format
**-> Figuring out if the delivery destination is in legal fly zone
**-> Finding out the no fly zones coming between current location and delivery destination in a specific order from drone location
**-> Merging two or more overlapping no fly zones for making shortest path calculations faster
**-> Making closest bounding boxes aroung irregular shaped no_fly zones to reduces the vertices to make calculations faster
**-> Making Using of Set, Map, Hashmap data structures for calcluations.
**-> Used Shapely, xml.etree, Matplot lib, numpy etc
**-> Calculating THE SHORTEST PATH FOR THE DELIVERY FROM CURRENT DRONE LOCATION
** Check the sample images in this file!
All Global Path Planning stuff!

The package contains following files and the discription is as follows

1) Path Planning Modules

-> file of libraries/modules for Main GPP to be implemented
-> Contains all modules that are implementations of concepts based on GPP algorithm
-> Any modules requiring modification must be modified only after having the GPP algorithm and its concepts in mind

2) No-Fly-Zones from kml

-> Gives the polygon(contains no-fly-zones as polygons) variable that can be stored as pickle or directly imported to scrubbing script
-> Source for this program is a kml map(text) file in which  polygons(lat-lon) of no-fly zones are given under attributes 'Coordinates'

3) Scrubbing

-> This file has input of polygon lists from a source file like kml, or from source of Airmap, Hover etc
-> The output is a list of regions which are unions of intersecting polygons. Also those polygons which are completly submerged
inside any ohter are completly removed from the output variable
-> The output is vaibale that can be stored as pickle
-> This is input for main Program for GPP
-> THE FILE INCLUDES A GENERAL ALGORITHM FOR FINDING UNION OF ALL INTERSECTING GEOMETRICAL AREAS

4) GPP Main

-> Finds the shortest path between two points (Customer location and drone location)
-> Input is the output of scrubbing script
-> Output is list of (x,y) pairs which are lat-lon

5) kml_poly.pickle

-> This is a pickle file which stores output of Polygons_from_kml and used as input to scrubbing program

6) Drones_no_fly_zones.kml

-> Kml map file from which polygons(no_fly_zones) are to be extracted 

Sample images and results

**Demostration of Merging overlapping no Flyzones**

These are no flyzones from the map file plotted on Matplotlib using which may or may not be merged into one whole no_fly_zones. 

Merging is necessary to reduce vertices and make calculations faster 
![Unmerged No flyzones](https://github.com/dhaval491/Trajectory-Planning-for-Autonomous-food-delivery-drones/blob/master/GPP__NoFlyZones.png)

-> Merged no fly zones from above

![Merged No flyzones](https://github.com/dhaval491/Trajectory-Planning-for-Autonomous-food-delivery-drones/blob/master/GPP_Merged_NoFlyZones.png)

**Once we have merged no fly zone in an irregular shap we need to make bounding boxes if there a more no fly zones to reduces the vertices**

![Bounding Box around a No fly zone](https://github.com/dhaval491/Trajectory-Planning-for-Autonomous-food-delivery-drones/blob/master/GPP_Bounding_boxes_around_No_fly_Zones.png)

**Sample No flyzones coming between source and destination to calculate the shortest path see the nest image to check which two no fly zone are considered

![No_flyzones](https://github.com/dhaval491/Trajectory-Planning-for-Autonomous-food-delivery-drones/blob/master/Sample%20Two%20no%20flyzone.png)

**Shortest Path for a sample of two no fly zones on the way

![Shortest path](https://github.com/dhaval491/Trajectory-Planning-for-Autonomous-food-delivery-drones/blob/master/GPP_Shotest_path.png)
