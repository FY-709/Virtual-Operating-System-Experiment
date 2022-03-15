import pymysql


class opdb(object):
    def __init__(self,h,u,p,d):
        self.con = pymysql.connect(host=h,user=u,passwd=p,port=3306,db=d)
        self.cursor = self.con.cursor()
    def save_result(self,id,status,result):   
        status.replace("'","\"")
        sql = "update cdata set c_status='%d',c_compile='%s',c_result='%s' where c_id='%s'"%(2,status,result,id)
        print("[I] "+ sql)
        self.cursor.execute(sql)
        self.con.commit()
    def init_data(self,id):
        sql1 = "select * from cdata where c_id='%s'"%(id)
        self.cursor.execute(sql1)
        r = self.cursor.rowcount
        if r == 0:
            sql2 = "insert into cdata(c_id,c_status) values ('%s','%d')"%(id,1)
        else:
            sql2 = sql = "update cdata set c_status='%d',c_compile='%s',c_result='%s' where c_id='%s'"%(1,"","",id)
        print("[I]" + sql1)
        print("[I]" + sql2)
        self.cursor.execute(sql2)
        self.con.commit()
