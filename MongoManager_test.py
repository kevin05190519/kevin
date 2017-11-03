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

    def update_score (self,view, data):
        col = get_score_collection(view)
        collection = self.db[col]
        result = collection.update_one({"title" : "5 stars"}, {"$set":{ "value" : data['5']}})
        if not result.raw_result['updatedExisting']: collection.insert_one({ "title" : "5 stars", "value" : data['5']})
        result = collection.update_one({"title" : "4 stars"}, {"$set":{ "value" : data['4']}})
        if not result.raw_result['updatedExisting']: collection.insert_one({ "title" : "4 stars", "value" : data['4']})
        result = collection.update_one({"title" : "3 stars"}, {"$set":{ "value" : data['3']}})
        if not result.raw_result['updatedExisting']: collection.insert_one({ "title" : "3 stars", "value" : data['3']})
        result = collection.update_one({"title" : "2 stars"}, {"$set":{ "value" : data['2']}})
        if not result.raw_result['updatedExisting']: collection.insert_one({ "title" : "2 stars", "value" : data['2']})
        result = collection.update_one({"title" : "1 star"}, {"$set":{ "value" : data['1']}})
        if not result.raw_result['updatedExisting']: collection.insert_one({ "title" : "1 star", "value" : data['1']})
        result = collection.update_one({"title" : "avg"}, {"$set":{ "value" : data['avg']}})
        if not result.raw_result['updatedExisting']: collection.insert_one({ "title" : "avg", "value" : data['avg']})


def get_collection(view):

        if view == 'ios':
            return MongoViews.MONGO_VIEW_IOS_REVIEWS
        else :
            return MongoViews.MONGO_VIEW_ANDROID_REVIEWS
def get_score_collection(view):

        if view == 'ios':
            return MongoViews.MONGO_VIEW_IOS_REVIEW_SCORE
        else:
            return MongoViews.MONGO_VIEW_ANDROID_REVIEW_SCORE







    # def importCSV(self):
    #     csv_path  = "{}/{}".format(os.path.dirname(os.path.realpath(__file__)),'daily_issues_status.csv')
    #     #write to CSV file
    #     with open(csv_path, 'rb') as f:
    #         r = csv.reader(f)
    #         olddata = [line for line in r]
    #
    #     csv_data = []
    #     csv_data.extend(olddata)
    #
    #     for item in csv_data:
    #         self.insertDailyIssuesCount(item)
