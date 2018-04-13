import psycopg2
from geopy.geocoders import  Nominatim
from geopy.geocoders import GoogleV3
from pygeocoder import Geocoder
#geolocator = Nominatim()
import time

key = "AIzaSyDCCnC6a4crMrXZ8iBdS5t7pFJa_PXm1eE"
geolocator = GoogleV3(api_key = key)

#google geocoder api key:  AIzaSyDCCnC6a4crMrXZ8iBdS5t7pFJa_PXm1eE
conn_string ="host='localhost' dbname='FYP' user='ciaran' password='password'"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

def dbUpdate(sname, id):
    try:
        cursor.execute("update locations set name = %s where location_id = %s;", (sname, id))
        conn.commit()
        print("update SUCCESS!")
    except psycopg2.DatabaseError as ex:
        print(str(ex))
        print("update error")
i = 0
j = 0





cursor.execute("select ST_AsText(geom), location_id from locations where name is null and highway like 'tertiary';")
all = cursor.fetchall()

for row in all:
    result = row[0]
    id = row[1]
    print(result)
    #print(id)

    list = result.split(',')
    list = list[1].split(',')
    list = list[0].split(')')
    coordinates = list[0].split('-')
    coordinates =coordinates[1] .split(" ")
    long = ("-"+coordinates[0])
    lat = (coordinates[1])

    string = lat + " " + long
    print(string)
    location = geolocator.geocode(string)

    print(location.address)
    place = location.address
    place = place.split(', Dublin')
    place = place[0]
    print(place)
    sname = location.raw['address_components'][0]['long_name']
    if (sname.isdigit()):
        sname = location.raw['address_components'][1]['long_name']

    if ('unnamed road' in sname):
        sname = place

    print(sname)
    if 'road' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'street' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'r1' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'r148' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'r8' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'm50' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'm7' in sname.lower():
        dbUpdate(sname, id)
        i += 1


    elif 'm11' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'm9' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'm1' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'm4' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'm8' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'n81' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'custom house quay' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'ormond quay' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'n7' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'A35' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    elif 'avenue' in sname.lower():
        dbUpdate(sname, id)
        i += 1
        
    elif 'n3' in sname.lower():
        dbUpdate(sname, id)
        i += 1

    else:
        print(location)


 #   dbUpdate(sname, id)
    j += 1
    print("Queried: " + str(j) + " items.")
    print("Inserted: " + str(i) + " items.")
    print("")
    print("")
    #time.sleep()


    #location = geolocator.reverse(string)
    #print(location)
    #address = location.address
    #print(address)


