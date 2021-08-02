
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
ckey = "MxKIdxywCntUBJETm9Xx8AiYw"
csecret = "pnxiuGSvKK7BTPe9sp7jSLUTk9Bxj5bDBlnw9hcauq9TjkiU2A"
atoken = "1420136431176015872-Y9G6EHRYnRNn5usrpxnlverpCVRsmN"
asecret = "bIF7xOijXfcgeoi05kOx8q5Qp50c9YlVxY40njO15GpKT"


#####################################

class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:

            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:1233tana@localhost:5984/')  #Conexion a couchdb
try:
    db = server.create('ecuador')#si no esta creada esa base de datos se crea
except:
    db = server['ecuador']#si a esta creada se trabaja con la misma

'''===============LOCATIONS=============='''

twitterStream.filter(locations=[-78.645645,-0.391087,-78.227066,-0.056557])#Tweets de Ecuador-Sangolqui
#twitterStream.filter(locations=[-4.2421,40.2163,-3.3104,40.7311])#tweets de España-Madrid
#twitterStream.filter(locations=[136.3355,35.1386,137.3168,35.5587])#tweets de Japon-Nagoya
'''===============tweets=============='''
#twitterStream.filter(track=['olympic', 'tokyo2021'])#Busca tweetes en relación a las palabras en el 'track'
