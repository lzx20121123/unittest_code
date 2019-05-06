import pymysql
import sys
sys.path.append('F:\\zk_unittest')
from  method.get_url import Get_ip
def MySql(sql):
    IP = Get_ip('sql','ip')
    db = pymysql.connect(IP, "entsafe", "entsafe", "shadu_ent", charset='utf8' )
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        data = cursor.fetchone()
        for i in data:
            #print 
            return i
    except:
        # 发生错误时回滚
        db.rollback()
 
    # 关闭数据库连接
    db.close()

if __name__ == "__main__":
    sq = 'select hash_key from report_group where name="sdsd"'
    re = MySql(sq)
    print (re)

