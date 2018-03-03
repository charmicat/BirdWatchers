from pymongo import MongoClient
import datetime


class MongoAccess(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['user-data']

        self.users = self.db['user-data']

    def insert(self, u_id, md5, followers):
        user_data = {"user_id": u_id, "date": datetime.datetime.utcnow(), "md5": md5, "followers": followers}
        data_id = self.users.insert_one(user_data).inserted_id

    def remove_old_data(self):
        #remove anything older than 30 days