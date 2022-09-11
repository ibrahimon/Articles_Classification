import falcon
import json 
import pickle
from wsgiref.simple_server import make_server

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

       


app = falcon.App()
app.add_route('/predict_category', ClassificationResource())

if __name__ == '_main_':
    with make_server(',8000,app') as httpd:
        print('server is running on port 8000...')
