import pymysql
from udn import settings

class UdnPipeline(object):
    def process_item(self, item, spider):
        return item

class Udn_Pipeline(object):
    def process_item(self, item, spider):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        psd = settings.MYSQL_PASSWORD
        db = settings.MYSQL_DB
        c = settings.CHARSET
        port = settings.MYSQL_PORT

        con = pymysql.connect(host=host, user=user, password=psd, db=db, charset=c, port=port)
        cue = con.cursor()
        print('mysql connect success')

        try:
            cue.execute(
                "insert into nba_news(title,content,img_url,url,author,post_time,pre_content) values(%s,%s,%s,%s,%s,%s,%s)",
                [item['title'], item['content'], item['img_url'], item['url'], item['author'], item['post_time'],item['pre_content']])
            print('insert success')


        except Exception as e:
            print('Insert error', e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item