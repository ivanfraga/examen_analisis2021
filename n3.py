import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

db_client = MongoClient("mongodb://localhost:27017")# conexion con compasss
my_db = db_client.get_database("examen_analisis")#Obtener base de datos previamente creada
my_posts=my_db['web_page']#Ubicar en coleccion previamente creada
url= 'https://www.marca.com/juegos-olimpicos/2021/07/31/61047c8b46163fca838b45a8.html'#pagina a usar
web_pag= requests.get(url)#conexion con dicha url
content= BeautifulSoup(web_pag.content, 'html.parser')#obtención del contenido de la pagina en el formato html

#titulares

soup= content.find_all('h2', class_='ue-c-article__subheadline')#Encuentra coincidencias de etiquetas 'h2' y clase respectiva
titulares= list()#lista donde se guardaran los datos
count=0
for i in soup:


    if count<=7: #control de numero de registros (8)
        titulares.append(i.text)#ingresar cada elemento(unicamente el texto) a la lista
    else:
        break
    count +=1
a={}
for i in range(len(titulares)):#bucle para guardarlos en formato json
    a={'noticia': titulares[i]}
    my_posts.insert_one(a)
    a={}

print(titulares)
