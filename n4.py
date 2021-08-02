from bs4 import BeautifulSoup
import pandas as pd
import requests
from facebook_scraper import get_posts
import couchdb
import json
import time
from pymongo import MongoClient

db_client = MongoClient("mongodb://localhost:27017")#Conexion a compass
my_db = db_client.get_database("examen_analisis")#Obtener base de datos(debe estar previamente creada)
my_posts=my_db['facebook']#Ubicar en coleccion (previamente creada)
i = 1

for post in get_posts('juegosolimpicos2021', pages=1000, extra_info=True):#Bucle para obtener datos de 'juegosolimpicos2021'
    print(i)#indica el número de post
    i = i + 1
    doc = {}#coleccion donde se guardaran el json
    mydate = post['time']

    try:
        #Dividir el post en diferentes elementos y guardarlos de forma clave-producto
        doc['texto'] = post['text']
        doc['date'] = mydate.timestamp()
        doc['likes'] = post['likes']
        doc['comments'] = post['comments']
        doc['shares'] = post['shares']
        try:
            doc['reactions'] = post['reactions']
        except:
            doc['reactions'] = {}

        doc['post_url'] = post['post_url']
        my_posts.insert_one(doc)# inserta la coleccion 'doc' en la coleccon indicada al principio
        print("guardado exitosamente")

    except Exception as e:
        print("no se pudo grabar:" + str(e))#Mensaje en caso de error
