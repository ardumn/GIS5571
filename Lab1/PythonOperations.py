import arcpy
import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as pet
!pip install geopandas fiona

arcpy.management.CreateFileGDB(r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1", "IntegratedGDB", "CURRENT")

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\IntegratedGDB.gdb"

# Set local variables
outWorkspace = "C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\Boundaries_of_Minnesota.shp"

# Use ListFeatureClasses to generate a list of shapefiles in the
#  workspace shown above.
fcList = arcpy.ListFeatureClasses()

# Execute CopyFeatures for each input shapefile
for shapefile in fcList:
    # Determine the new output feature class path and name
    outFeatureClass = os.path.join(outWorkspace, shapefile.strip(".shp"))
    arcpy.CopyFeatures_management(shapefile, outFeatureClass)

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\IntegratedGDB.gdb"

# Set local variables
outWorkspace = "C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\MnDOT_Roadway_Routes_in_Minnesota.shp"

# Use ListFeatureClasses to generate a list of shapefiles in the
#  workspace shown above.
fcList = arcpy.ListFeatureClasses()

# Execute CopyFeatures for each input shapefile
for shapefile in fcList:
    # Determine the new output feature class path and name
    outFeatureClass = os.path.join(outWorkspace, shapefile.strip(".shp"))
    arcpy.CopyFeatures_management(shapefile, outFeatureClass)

arcpy.conversion.FeatureClassToGeodatabase("MnDOT_Roadway_Routes_in_Minnesota;Boundaries_of_Minnesota", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb")

arcpy.ListFiles()

arcpy.ListFeatureClasses()

MnDOT_Roadway_Routes_in_Minnesota = "C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\IntegratedGDB.gdb"

arcpy.Describe(MnDOT_Roadway_Routes_in_Minnesota).spatialReference

fields = ['ROUTE_ID',
         'ROUTE_NAME',
         'ROUTE_LANE']

with arcpy.da.SearchCursor(MnDOT_Roadway_Routes_in_Minnesota, fields) as cursor:
    for row in cursor:
        if '0400006594470001-I' in row[2]:
            print(row)

df = pd.DataFrame([row for row in arcpy.da.SearchCursor(MnDOT_Roadway_Routes_in_Minnesota, fields)])

df.head()

arcpy.management.Project("CityofMinneapolisBoundaryDowntown_XYTableToPoint", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\MyProject1\MyProject1.gdb\CityofMinneapolisDown_Projec", 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', None, 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', "NO_PRESERVE_SHAPE", None, "NO_VERTICAL")

arcpy.management.Project("DowntownMinneapolisResturants_XYTableToPoint", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\MyProject1\MyProject1.gdb\CityofMinneapolisRest_Projec", 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', None, 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', "NO_PRESERVE_SHAPE", None, "NO_VERTICAL")

arcpy.analysis.SpatialJoin("CityofMinneapolisRest_Projec", "Boundaries_of_Minnesota", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb\CityofMinneapolisRestDowntownSJ", "JOIN_ONE_TO_ONE", "KEEP_ALL", 'Name "Name" true true false 8000 Text 0 0,First,#,CityofMinneapolisRest_Projec,Name,0,8000;Latitude "Latitude" true true false 8 Double 0 0,First,#,CityofMinneapolisRest_Projec,Latitude,-1,-1;Longitude "Longitude" true true false 8 Double 0 0,First,#,CityofMinneapolisRest_Projec,Longitude,-1,-1;STATE_FIPS "STATE_FIPS" true true false 10 Long 0 10,First,#,Boundaries_of_Minnesota,STATE_FIPS,-1,-1;STATE_GNIS "STATE_GNIS" true true false 10 Long 0 10,First,#,Boundaries_of_Minnesota,STATE_GNIS,-1,-1;STATE_NAME "STATE_NAME" true true false 254 Text 0 0,First,#,Boundaries_of_Minnesota,STATE_NAME,0,254;SHAPE_Leng "SHAPE_Leng" true true false 19 Double 0 0,First,#,Boundaries_of_Minnesota,SHAPE_Leng,-1,-1;SHAPE_Area "SHAPE_Area" true true false 19 Double 0 0,First,#,Boundaries_of_Minnesota,SHAPE_Area,-1,-1', "WITHIN", None, '')

arcpy.analysis.SpatialJoin("CityofMinneapolisDown_Projec", "Boundaries_of_Minnesota", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb\CityofMinneapolisDowntownSJ", "JOIN_ONE_TO_ONE", "KEEP_ALL", None, "WITHIN", None, '')


