#!/usr/bin/python3
#coding:utf-8
import MySQLdb
import configparser

def mysql_execute(sql,flag):
    """
    执行sql命令
    """
    #:获取配置信息
    path = 'mysql.ini'
    config = configparser.ConfigParser()
    config.read(path)
    host = config.get("Settings","host")
    user = config.get("Settings","user")
    passwd = config.get("Settings","passwd")
    port = config.get("Settings","port")

    #:连接数据库
    try:
        conn = MySQLdb.connect(host=host, user=user,passwd=passwd,port=int(port))
        cur = conn.cursor()
        conn.select_db('network')

        #:执行sql命令
        cur.execute(sql)

        #:获取结果
        if flag == 'fetchall':
            result = cur.fetchall()
        elif flag == 'fetchone':
            result = cur.fetchone()
        elif flag == 'commit':
            conn.commit()
            result = 'commit'
        else:
            result = 'Failed'
    except MySQLdb.Error as e:
        print("Mysql Error%d:%s" % (e.args[0],e.args[1]))
        result = 'Failed'
    finally:
    
        #:关闭数据库连接
        cur.close()
        conn.close()

        return result

if __name__ == '__main__':
    sql = 'select * from ips'
    for i in range(5):
        print(mysql_execute(sql,'fetchone')) 
