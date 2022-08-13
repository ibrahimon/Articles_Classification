

import json
import pickle
from wsgiref.simple_server import make_server

import falcon
import psycopg2
import psycopg2.extras
import logging
import mylib
import platform


#Buliding ARTICLES database
conn = psycopg2.connect(dbname = Articles, user= Ibrahim000, password = pass00pass, host = DB_Host)

#Logging Info
os_name = platform.uname()[0].lower()
if os_name == "windows":
   time = get_win_login_time()
   date = get_win_login_date()

    


def classify_text(text):
       file_name = 'resources/svm_modle.sav'
       loaded_model = pickle.load(open(file_name, 'rb'))
       predicted_svm_loaded = loaded_model.predict([article_body])
       return predicted_svm_loaded[0]
        

class ClassificationResource:
    
    def on_post(self, req, resp):
        raw_input = req.bounded_stream.read()
        article_body = raw_json


        predicted_category = classify_text(article_body)


        #login
        resp.status = falcon.HTTP_200
        resp.body = json.dump({
            predicted_category: predicted_category
        })

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('CREATE TABLE ARTICLES (Date integer, Date integer, Title text, Body text, Category Text);')
    cur.execute('INSERT INTO ARTICLES (Date) Values(%d/%d/%d),(date)')
    cur.execute('INSERT INTO ARTICLES (time) Values(%d/%d/%d),(time)')
    cur.execute('INSERT INTO ARTICLES (Body) Values(%s),(article_body)')
    cur.execute('INSERT INTO ARTICLES (Category) Values(%s),(predicted_category)')


    conn.commit()




app = falcon.App()
app.add_route('/predict_category', ClassificationResource())

if __name__ == '_main_':
    with make_server(',8000,app') as httpd:
        print('server is running on port 8000...')

cur.close()
conn.close()
