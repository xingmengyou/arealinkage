import json
import time

import pymysql

# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citys_linkages.settings")# project_name 项目名称
# django.setup()


class Datasbase(object):

    def __init__(self, table):
        self.id = ''
        self.code = ''
        self.name = ''
        self.type = ''
        self.parent_id = ''
        self.parent_ids = ''
        self.sort = ''
        self.del_flag = ''
        self.db = pymysql.connect(host='localhost', user='root', password="123456",
                                  database='test', port=3306)
        self.cursor = self.db.cursor()
        self.table = table

    def save(self, lts):
        # sql = """INSERT INTO sys_areas (id,code,name,type,parent_id,parent_ids,sort,del_flag) select

        # %s,%s,%s,%s,%s,%s,%s,%s where not exists(select code from sys_areas where code=%s)"""
        sql = """INSERT INTO %s """ % self.table + """(pid,code,name,type,parent_id_id,parent_ids,sort,del_flag) VALUES 
        (%s,%s,%s,%s,%s,%s,%s,%s)"""
        # params = (self.id, self.code, self.name, self.type, self.parent_id, self.parent_ids,
        #           self.sort, self.del_flag)
        params = lts

        self.cursor.executemany(sql, params)
        self.db.commit()


def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)

    return decor


@timer
def save_sql(f):
    db = Datasbase('village')
    f = open(f, 'r', encoding='utf-8')
    lts = json.load(f)
    print(lts[:3])
    lt = list()
    for l in lts:

        lt.append((l['id'], l['code'], l['name'], l['type'], l['parent_id'],
                   l['parent_ids'], l['sort'], l['del_flag']))
    db.save(lt)


if __name__ == "__main__":
    save_sql('json/villages.json')





