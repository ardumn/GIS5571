import requests
import arcpy
import pandas
import json

API_Key = "AIzaSyB3E4lw0kwP4oLADoLkwBktN_sBovHbLFE"

Google_Places_URL_Base = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

Input_Place = "Downtown Minneapolis Restaurants"

Formatted_Input = Input_Place.replace (" ", "%20")
Formatted_Input

#List of Parameters

Input_Parameters = "?input=" + Formatted_Input
Input_Type = "&inputtype=textquery"
Field_Parameters = "&fields=photos, formatted_adress, name, rating, opening_hours, geometry"
Key_Parameters = "&key=" + API_Key

Google_Path = Google_Places_URL_Base+Input_Parameters+Input_Type+Field_Parameters+Key_Parameters
Google_Path

Google_RequestObject = requests.get(Google_Path)
print(Google_RequestObject)

payload={}
headers = {}

Google_Places_URL_Base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.97658%2C-93.2761&radius=1000&type=downtown&keyword=downtown&key=AIzaSyB3E4lw0kwP4oLADoLkwBktN_sBovHbLFE"

response = requests.request("GET", Google_Places_URL_Base, headers=headers, data=payload)

print(response.text)
r_json_restaurants=response.json()

df=pandas.DataFrame(columns=("Name", "Latitude","Longitude"))
r_json = response.json()["results"]
for feature in range(len(r_json)):
    name=[r_json[feature]["name"]]
    Latitude=[r_json[feature]["geometry"]["location"]["lat"]]
    Longitude=[r_json[feature]["geometry"]["location"]["lng"]]
    
    df.loc[feature]=name+Latitude+Longitude
    
df.head()

arcpy.conversion.TableToTable(r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\DowntownMinneapolis.csv", r"C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\IntegratedGDB.gdb", "DowntownMinneapolisResturants", '', r'Name "Name" true true false 8000 Text 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\DowntownMinneapolis.csv,Name,0,8000;Latitude "Latitude" true true false 8 Double 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\DowntownMinneapolis.csv,Latitude,-1,-1;Longitude "Longitude" true true false 8 Double 0 0,First,#,C:\Users\Alexander Danielson\Desktop\Fall 2022Spring2023\ArcGIS I\Lab1\DowntownMinneapolis.csv,Longitude,-1,-1', '')


