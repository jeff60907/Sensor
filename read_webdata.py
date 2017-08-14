import requests
res = requests.get('http://192.168.XX.XX/')
#print(res.content)

string = res.content
Temperature = string[14:16]
Humidity = string[29:31]
Soil = string[49:len(string)-1]
Sensor = Temperature + ',' + Humidity + ',' + Soil
#print Temperature,Humidity,Soil
print Sensor
