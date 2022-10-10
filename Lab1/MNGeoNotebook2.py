import arcpy
import requests
import zipfile
import io

arcpy.env.workspace = r'C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\MyProject1'

arcpy.env.workspace

test_link = r'https://gisdata.mn.gov/dataset/bdry-state'

req_obj = requests.get(test_link)

req_obj.text

download_link = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dot/bdry_state/fgdb_bdry_state.zip'

download_link

output = requests.post(download_link)

slashstuff = output.content

zipp = zipfile.ZipFile(io.BytesIO(slashstuff))

zipp.extractall(r'C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\MyProject1')


