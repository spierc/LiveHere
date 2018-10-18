import urllib.request
import os

cwd = os.getcwd()

print("downloading LiveHere data files to this directory. This may take some time")

#URLs of each resource. format: [first CP score]_[first attribute]_[first url]
road = "http://data.ottawa.ca/dataset/82391b5b-974c-473e-87bd-4c5e24de9deb/resource/a65e0b1e-ab26-418d-8afb-9fbbf9d53c0b/download/road-segments.json"

urllib.request.urlretrieve(road, cwd+"roads.json")

#1_2_1

hydroline = "http://data.ottawa.ca/dataset/c26802f2-96ed-4b2e-9d56-f834680b9984/resource/2cd3c332-3b55-4430-b23f-91c7d0e7cbee/download/hydrolines.json"

urllib.request.urlretrieve(hydroline, cwd+"hydrolines.json") 

#1_4_1

restos = "http://app01.ottawa.ca/inspections-opendata/yelp_ottawa_all_healthscores.zip"

urllib.request.urlretrieve(restos, cwd+"restos.zip") 


police = "https://moto.data.socrata.com/dataset/Ottawa-Police/uacw-px76"

urllib.request.urlretrieve(police, cwd+"police.csv") 


parks = "http://data.ottawa.ca/dataset/c6e1a245-f052-43fa-9f5d-8fe13ea79ac3/resource/0c40aa09-9133-4625-a0fa-955b8b720f9f/download/parks.json"

urllib.request.urlretrieve(parks, cwd+"parks.json") 

#5_1_1 = 1_6_1

fires = "http://cwfis.cfs.nrcan.gc.ca/datamart/download/nfdbpnt?token=5d4c99e64194c5a97e612a2c26a9aacb"

urllib.request.urlretrieve(fires, cwd+"fires.txt") 

