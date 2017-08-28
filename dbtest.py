#coding:utf-8

import pymongo

uri = "mongodb://172.30.31.203:27017"
client=pymongo.MongoClient(uri)
database=client['upDashBoard']
collection=database['ios_review']
s=collection.find({})
# collection.insert(mydict)

#database.drop_collection('ios_review_score')

m=1
print database.collection_names()

for doc in collection.find():
    print m

    m+=1
    print(doc)