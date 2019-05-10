import pymysql
import json

def zip_cloud(request):
    con = pymysql.connect('35.185.191.185','prima','123456','python')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tb_index WHERE ket='zip cloud'")
        table = cur.fetchall()
    return json.dumps(table)
 