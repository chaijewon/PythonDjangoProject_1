from django.db import models

# Create your models here.
import oracledb as db
def getConnection():
    try:
        conn=db.connect("hr/happy@localhost:1521/XE")
    except Exception as e:
        print(e)
    return conn
def disConnection(conn,cur):
    try:
        cur.close()
        conn.close()
    except Exception as e:
        print(e)

def recipeListData(page):
    try:
        rowSize=12
        start=(rowSize*page)-(rowSize-1)
        end=rowSize*page
        #연결
        conn=getConnection()
        cur=conn.cursor()

        sql=f"""
              SELECT no,title,poster,chef,num
              FROM (SELECT no,title,poster,chef,rownum as num
              FROM (SELECT /*+ INDEX_ASC(recipe recipe_no_pk)*/no,title,poster,chef
              FROM recipe WHERE no IN(SELECT no FROM recipe INTERSECT SELECT no FROM recipeDetail)))
              WHERE num BETWEEN {start} AND {end}
             """
        cur.execute(sql)
        list=cur.fetchall()
        cur.close()
        cur=conn.cursor()
        sql="""
             SELECT CEIL(COUNT(*)/12.0) FROM recipe
             WHERE no IN(SELECT no FROM recipe INTERSECT SELECT no FROM recipeDetail) 
            """
        cur.execute(sql)
        total=cur.fetchone()
        #(100,) => 데이터베이스는 무조건 튜플
    except Exception as e:
        print(e)
    finally:
        disConnection(conn,cur)
    return list,total[0]
'''
NO           NOT NULL NUMBER         
POSTER       NOT NULL VARCHAR2(4000) 
TITLE        NOT NULL VARCHAR2(1000) 
CHEF         NOT NULL VARCHAR2(1000) 
CHEF_POSTER  NOT NULL VARCHAR2(1000) 
CHEF_PROFILE NOT NULL VARCHAR2(1000) 
INFO1        NOT NULL VARCHAR2(100)  
INFO2        NOT NULL VARCHAR2(100)  
INFO3        NOT NULL VARCHAR2(100)  
CONTENT      NOT NULL VARCHAR2(4000) 
FOODMAKE     NOT NULL CLOB           
DATA                  CLOB     
'''
def recipeDetailData(no):
    try:
        conn=getConnection()
        cur=conn.cursor()
        sql=f"""
               SELECT no,title,chef,chef_poster,chef_profile,
               info1,info2,info3,content,poster,foodmake,data
               FROM recipedetail
               WHERE no={no}
            """
        cur.execute(sql)
        recipe_detail=cur.fetchone()
        #CLOB (Object => str)
        rmake=''.join(recipe_detail[-2].read())
        rdata=''.join(recipe_detail[-1].read())
    except Exception as e:
        print(e)
    finally:
        disConnection(conn,cur)

    return recipe_detail,rmake,rdata