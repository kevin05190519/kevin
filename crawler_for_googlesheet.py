#coding:utf-8
#from MongoManager_test import MongoManager

import json
import gspread

import logging
# import numpy as np
# import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials as SAC
GDriveJSON = '/Users/kkbox/downloads/tryfi-fad4510c2527.json'
GSpreadSheet = 'Tryfi寶貝精品嚴選成立規劃'

#
# x = np.linspace(0, 2 * np.pi, 100)
# y1, y2 = np.sin(x), np.cos(x)
#
# plt.plot(x, y1, c='r', ls='--', lw=3)
# plt.plot(x, y2, c='#526922', ls='-.')
# plt.show()
#

scope = ['https://spreadsheets.google.com/feeds']
key = SAC.from_json_keyfile_name(GDriveJSON, scope)
gc = gspread.authorize(key)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1-X2XuteWoDZkvDHJ39Mx-QV5zioddPXZIQA5nrM_cOQ/edit#gid=820905649')
worksheet = sht2.get_worksheet(4)
values_list = worksheet.col_values(2)
#count={"count_store":0,"count_gender":0,"count_clothes":0,"count_style":0,"count_color":0,"count_size":0}


def get_count_store():
    worksheet = sht2.get_worksheet(2)
    store_list = worksheet.col_values(2)
    store_json = {}
    for store_id in store_list:
        count_store = 0
        for values in values_list:
            if values and store_id is not "":
                if values[0:2] == store_id:
                    count_store+=1
                store_json.update({store_id:count_store})
    print json.dumps(store_json)

def get_count_gender():
    worksheet = sht2.get_worksheet(2)
    gender_list = worksheet.col_values(5)
    gender_json = {}
    for gender_id in gender_list:
        count_gender = 0
        for values in values_list:
            if values and gender_id is not "":
                if values[3] == gender_id:
                    count_gender+=1
                gender_json.update({gender_id:count_gender})
    print json.dumps(gender_json)


def get_count_season():
    worksheet = sht2.get_worksheet(2)
    season_list = worksheet.col_values(7)
    season_json = {}
    for season_id in season_list:
        count_season = 0
        for values in values_list:
            if values and season_id is not "":
                if values[5:7] == season_id:
                    count_season+=1
                    season_json.update({season_id:count_season})
    print json.dumps(season_json)

def get_count_clothes():
    worksheet = sht2.get_worksheet(2)
    clothes_list = worksheet.col_values(9)
    clothes_json = {}
    for clothes_id in clothes_list:
        count_clothes = 0
        for values in values_list:
            if values and clothes_id is not "":
                if values[8] == clothes_id:
                    count_clothes+=1
                    clothes_json.update({clothes_id:count_clothes})
    print json.dumps(clothes_json)

def get_count_style():
    worksheet = sht2.get_worksheet(2)
    style_list = worksheet.col_values(11)
    style_json = {}
    for style_id in style_list:
        count_style = 0
        for values in values_list:
            if values and style_id is not "":
                if values[10:13] == style_id:
                    count_style+=1
                    style_json.update({style_id:count_style})
    print json.dumps(style_json)

def get_count_color():
    worksheet = sht2.get_worksheet(2)
    color_list = worksheet.col_values(14)
    color_json = {}
    for color_id in color_list:
        count_color = 0
        for values in values_list:
            if values and color_id is not "":
                if values[17:19] == color_id:
                    count_color+=1
                    color_json.update({color_id:count_color})
    print json.dumps(color_json)

def get_count_size():
    worksheet = sht2.get_worksheet(2)
    size_list = worksheet.col_values(16)
    size_json = {}
    for size_id in size_list:
        count_size = 0
        for values in values_list:
            if values and size_id is not "":
                if values[20:26] == size_id:
                    count_size+=1
                    size_json.update({size_id:count_size})
    print json.dumps(size_json)

def get_all_count():
    get_count_gender()
    get_count_store()
    get_count_clothes()
    get_count_style()
    get_count_color()
    get_count_size()
    #test()
if __name__ == "__main__":
    get_all_count()


