import pymongo
from pymongo import MongoClient
from datetime import datetime

import csv, os

class MongoViews:
    MONGO_VIEW_STORE="store"
    MONGO_VIEW_GENDER = "gender"
    MONGO_VIEW_CLOTHES = "clothes"
    MONGO_VIEW_STYLE = "style"
    MONGO_VIEW_COLOR="color"
    MONGO_VIEW_SIZE ="size"
class MongoManager:

    DBURL = "mongodb://127.0.0.1:27017"
    # DBURL = 'mongodb://utapass-jenkins.kkinternal.com:27017'

    client = None
    db = None

    def __init__(self):
        self.client = MongoClient(self.DBURL)
        self.db = self.client['kevin']
        return None



    def query_is_comments_existed(self, view,data):

        col = get_collection(view)
        collection = self.db[col]
        result = collection.find_one( {"score":  data["score"] ,
                                   "title":  data["title"] ,
                                   "createdDate":  data["date"],
                                   "comment": data["comment"]
                                   })
        return result != None

    def insert_reviews (self,view, data):
        col = get_collection(view)
        collection = self.db[col]
        result = collection.insert_one(
                {
                    "title" : data['title'],
                    "score": data['score'],
                    "createdDate": data['date']
                })


def get_collection(view):


        if view == 'ios':return MongoViews.MONGO_VIEW_STORE
        if view == 'ios':return MongoViews.MONGO_VIEW_GENDER
        if view == 'ios':return MongoViews.MONGO_VIEW_CLOTHES
        if view == 'ios':return MongoViews.MONGO_VIEW_STYLE
        if view == 'ios':return MongoViews.MONGO_VIEW_COLOR
        else :return MongoViews.MONGO_VIEW_SIZE





