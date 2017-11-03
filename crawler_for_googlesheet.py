#coding:utf-8
#from MongoManager_test import MongoManager

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

GDriveJSON = '/Users/kkbox/downloads/tryfi-fad4510c2527.json'
GSpreadSheet = 'Tryfi寶貝精品嚴選成立規劃'



scope = ['https://spreadsheets.google.com/feeds']
key = SAC.from_json_keyfile_name(GDriveJSON, scope)
gc = gspread.authorize(key)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1-X2XuteWoDZkvDHJ39Mx-QV5zioddPXZIQA5nrM_cOQ/edit#gid=820905649')
worksheet_page4 = sht2.get_worksheet(4)
values_list = worksheet_page4.col_values(2)
worksheet_page2 = sht2.get_worksheet(2)


def set_count():
    get_count_store(2, 0, 2)
    get_count_gender(5,3)
    get_count_season(7,5,7)
    get_count_clothes(9,8)
    get_count_style(11,10,13)
    get_count_color(14,17,19)
    get_count_size(16,20,26)

def get_count_store(col,x,y):
    store_list = worksheet_page2.col_values(col)
    store_json = {}
    for store_id in store_list:
        count_store = 0
        for values in values_list:
            if values and store_id is not "":
                if values[x:y] == store_id:
                    count_store+=1
                store_json.update({store_id:count_store})
    print json.dumps(store_json)

def get_count_gender(col,x):
    gender_list = worksheet_page2.col_values(col)
    gender_json = {}
    for gender_id in gender_list:
        count_gender = 0
        for values in values_list:
            if values and gender_id is not "":
                if values[x] == gender_id:
                    count_gender+=1
                gender_json.update({gender_id:count_gender})
    print json.dumps(gender_json)


def get_count_season(col,x,y):
    season_list = worksheet_page2.col_values(col)
    season_json = {}
    for season_id in season_list:
        count_season = 0
        for values in values_list:
            if values and season_id is not "":
                if values[x:y] == season_id:
                    count_season+=1
                    season_json.update({season_id:count_season})
    print json.dumps(season_json)

def get_count_clothes(col,x):
    clothes_list = worksheet_page2.col_values(col)
    clothes_json = {}
    for clothes_id in clothes_list:
        count_clothes = 0
        for values in values_list:
            if values and clothes_id is not "":
                if values[x] == clothes_id:
                    count_clothes+=1
                    clothes_json.update({clothes_id:count_clothes})
    print json.dumps(clothes_json)

def get_count_style(col,x,y):
    style_list = worksheet_page2.col_values(col)
    style_json = {}
    for style_id in style_list:
        count_style = 0
        for values in values_list:
            if values and style_id is not "":
                if values[x:y] == style_id:
                    count_style+=1
                    style_json.update({style_id:count_style})
    print json.dumps(style_json)

def get_count_color(col,x,y):
    color_list = worksheet_page2.col_values(col)
    color_json = {}
    for color_id in color_list:
        count_color = 0
        for values in values_list:
            if values and color_id is not "":
                if values[x:y] == color_id:
                    count_color+=1
                    color_json.update({color_id:count_color})
    print json.dumps(color_json)

def get_count_size(col,x,y):
    size_list = worksheet_page2.col_values(col)
    size_json = {}
    for size_id in size_list:
        count_size = 0
        for values in values_list:
            if values and size_id is not "":
                if values[x:y] == size_id:
                    count_size+=1
                    size_json.update({size_id:count_size})
    print json.dumps(size_json)

def get_all_count():
    set_count()

if __name__ == "__main__":
    get_all_count()


