
import couchdb
import pymongo
from pymongo import MongoClient
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json




server = couchdb.Server('http://admin:1233tana@localhost:5984/')  #Conexion a couchdb
try:
    db = server.create('ecuador')#si no esta creada esa base de datos se crea
except:
    db = server['ecuador']#si a esta creada se trabaja con la misma

db_client = MongoClient("mongodb://localhost:27017")# conexion con compasss
my_db = db_client.get_database("examen_analisis")#Obtener base de datos previamente creada
my_posts=my_db['ecuador']

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) )
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
a ={}#guardar json
x=0#validación de campo
for element in db:
    doc = str(db[element])
    clase=[]
    info=[]
    limpio = str(doc[find_1st(doc, '{') + 1:find_2nd(doc, '}')])
    limpio1= limpio.split(':',1)#separa datos (campo-contenido)
    for elemet1 in limpio1:
        elemet1 = elemet1.replace("'", " ")#reemplazo de comillas simples por espacio
        elemet1 = elemet1.strip()#eliminar los espacios (Al principio y final)
        if x==0:#verificamos si es campo
            clase.append(elemet1)#agremos a lista clase
            x=x+1
        else:
            info.append(elemet1)#sino, es contenido y se agrega a lista info
    x=0#reanuda
    for el in range(len(clase)):#bucle creación diccionario
        a={
            clase[el]:info[el]#cada elemento de campo y contenido se agregan al diccionario a
        }
        print(a)
        my_posts.insert_one(a)#guarda cada unoen la colección previamente creada
        a={}



