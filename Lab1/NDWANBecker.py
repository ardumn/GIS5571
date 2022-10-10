import arcpy
import requests
import pandas as pd
import csv
import os

NDAWN_URL = "https://ndawn.ndsu.nodak.edu/table.csv"

Parameters = {
    "station" : "Ada",
    "variable" : "mdavt",
    "dfn" : "",
    "year" : "2022",
    "ttype" : "daily",
    "quick_pick" : "",
    "begin_date" : "2022-10",
    "count" : "12"}
Request_Response = requests.get(NDAWN_URL, params  = Parameters)

with open("C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\NDAWNBECKER.csv" , "w") as newCSV_txt:
    newCSV_txt.write(Request_Response.content.decode('utf-8'))

Peek_In = pd.read_csv(r'C:\\Users\\Alexander Danielson\\Desktop\\Fall 2022Spring2023\\ArcGIS I\\Lab1\\NDAWNBECKER.csv', on_bad_lines = "skip")
Peek_In.head()

arcpy.conversion.TableToTable(r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb", "NDAWNBECKER", '', r'edu "edu" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Data from North Dakota Agricultural Weather Network https://ndawn.ndsu.nodak.edu,0,8000;Field2 "Field2" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field2,0,8000;Field3 "Field3" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field3,0,8000;Field4 "Field4" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field4,0,8000;Field5 "Field5" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field5,0,8000;Field6 "Field6" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field6,0,8000;Field7 "Field7" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field7,0,8000;Field8 "Field8" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field8,0,8000;Field9 "Field9" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\BECKER_NDAWN.csv,Field9,0,8000', '')


