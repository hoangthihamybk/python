import  pymysql
import traceback

try:
    conn = pymysql.connect(user="root",password="", host="127.0.0.1",port=3306,database="admage_fam8_standard", charset="utf8")
    print("Ket noi thanh cong")
except:
    traceback.print_exc()
    print("Ket noi khong thanh cong")
