import requests, json

address = "Universidade de Aveiro, Rua do Crasto, Glória, Aveiro, Baixo Vouga, Centro, 3810-193, Portugal"

serviceurl = "https://nominatim.openstreetmap.org/search.php?format=json&q=%s" % address

r = requests.get(serviceurl)

print(r.status_code)

data = json.dumps(r.json(), indent=4)
print(data)

avg_latitude = (float(r.json()[0]["boundingbox"][0])+float(r.json()[0]["boundingbox"][1]))/2.0
avg_longitude = (float(r.json()[0]["boundingbox"][2])+float(r.json()[0]["boundingbox"][3]))/2.0

print("Media latitudes: %f " %avg_latitude)
print("Media longitudes: %f " %avg_longitude)