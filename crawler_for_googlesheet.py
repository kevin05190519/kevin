#coding:utf-8
from MongoManager_test import MongoManager

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
GDriveJSON = '/Users/kkbox/downloads/tryfi-fad4510c2527.json'
GSpreadSheet = 'Tryfi寶貝精品嚴選成立規劃'



scope = ['https://spreadsheets.google.com/feeds']
key = SAC.from_json_keyfile_name(GDriveJSON, scope)
gc = gspread.authorize(key)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1-X2XuteWoDZkvDHJ39Mx-QV5zioddPXZIQA5nrM_cOQ/edit#gid=820905649')
worksheet = sht2.get_worksheet(4)
values_list = worksheet.col_values(2)
#count={"count_store":0,"count_gender":0,"count_clothes":0,"count_style":0,"count_color":0,"count_size":0}
store=[]

def get_store_id():
    worksheet = sht2.get_worksheet(3)
    global store_list
    store_list = worksheet.col_values(2)





def get_count_store():
    get_store_id()
    store_json = {}
    for store_id in store_list:
        if store_id is not "":

            count_store=0
            for a in values_list:
                if a[0:2] == store_id:
                    count_store+=1

            store_json.update()

    print store_json











def get_all_count():

    get_count_store()

if __name__ == "__main__":
    get_all_count()


