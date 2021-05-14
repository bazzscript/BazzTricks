from geopy import GoogleV3
place = "your adrress"
location = GoogleV3().geocode(place)
print(location.address)
print(location.location)