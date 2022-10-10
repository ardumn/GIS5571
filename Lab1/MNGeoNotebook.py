import arcpy
import requests
import zipfile
import io

arcpy.env.workspace = r'C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb'

arcpy.env.workspace

test_link = r'https://gisdata.mn.gov/dataset/trans-roads-centerlines'

req_obj = requests.get(test_link)

req_obj.text

download_link = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dot/trans_roads_centerlines/shp_trans_roads_centerlines.zip'

download_link

output = requests.post(download_link)

slashstuff = output.content

zipp = zipfile.ZipFile(io.BytesIO(slashstuff))

zipp.extractall(r'C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb')




