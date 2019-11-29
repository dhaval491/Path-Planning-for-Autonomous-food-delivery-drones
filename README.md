# global-path-planning

All Global Path Planning stuff!

The package contains following files and the discription is as follows

1) Path Planning Modules

-> file of libraries/modules for Main GPP to be implemented
-> Contains all modules that are implementations of concepts based on GPP algorithm
-> Any modules requiring modification must be modified only after having the GPP algorithm and its concepts in mind

2) Polygons from kml

-> Gives the polygon variable that can be stored as pickle or directly imported to scrubbing script
-> Source for this program is a kml text file in which  polygons(lat-lon) of no-fly zones are given under attributes 'Coordinates'

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
