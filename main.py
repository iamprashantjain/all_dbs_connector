#we are going to create a python package which is a folder consist of multiple files
#we are going to host our code as python package which can be used & installed using pip install
#mongodb is a nosql dbs which we use to store data in dictionary format

#


import pymongo

#provide mongodb localchost url to connect python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/nuerolabdb")


#dbname
dataBase = client["nuerolabDB"]

#collection
collection = dataBase['products']

#sampledata
d = {'company_name':'inuron',
     'product':'affordable ai',
     'courseoffered':'ml with deployment'}


#insert
rec = collection.insert_one(d)

#verify
all_record = collection.find()

for idx, record in enumerate(all_record):
    print(f"{idx}:{record}")