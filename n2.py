
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
    db = server.create('olympic_games')#si no esta creada esa base de datos se crea
except:
    db = server['olympic_games']#si a esta creada se trabaja con la misma

'''===============LOCATIONS=============='''

# twitterStream.filter(locations=[11.4037,41.7901,13.9414,43.568])
twitterStream.filter(track=['olympic', 'tokyo2021'])#Busca tweetes en relación a las palabras en el 'track'
