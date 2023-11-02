#Carga Librerias
import pandas as pd
import numpy as np

import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import matplotlib.pyplot as plt
import seaborn as sns


#instanciar la aplicación

app = FastAPI()

#Ruta
#http://127.0.0.1:8000

#Documentacion: 
#http://127.0.0.1:8000/docs


#-------------------------------Diseno Pagina Web----------------------------------

@app.get("/", response_class=HTMLResponse)
async def incio ():
    principal= """
    <!DOCTYPE html>
    <html>
        <head>
            <title>API Steam</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Henry Assesment</h1>
            <p>Bienvenido a la API de Steam donde se pueden hacer diferentes consultas sobre la plataforma de videojuegos.</p>
            <p>INSTRUCCIONES:</p>
            <p>Escriba <span style="background-color: lightgray;">/docs</span> a continuación de la URL actual de esta página para interactuar con la API</p>
            <p>Consulte en el siguiente enlace:<a href="https://pi1-steamgames-deploy-jimefioni.onrender.com/docs/">{{FastAPI}}</a></p>
            <p>El desarrollo de este proyecto esta en <a href="https://github.com/a1ternocles/Henry-Assesment.git"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
            <p>Andres Ruiz - 2023 -</p>
        </body>
    </html>
        """    
    return principal

#-------------------------------Funciones----------------------------------

#Primera Funcion-----------------------------------------------------------

@app.get("/PlayTimeGenre/{genero}", name = "Tiempo De Juego Por Genero")
#* def PlayTimeGenre( genero : str )
# return **Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}**
def PlayTimeGenre(genero: str):
    genero_dicc= {}

    try:
        if type(genero) == str:

            genero = genero.lower().title()
            playtime_data = pd.read_parquet("Henry-Assesment\data\playtime_data")
            lista_genero = playtime_data["genres"].unique()

            if genero in lista_genero:

                data_genero = playtime_data[playtime_data["genres"] == genero]
                data_horas = data_genero.groupby("release_year")["playtime_forever"].sum()
                anio_max = data_horas.idxmax()

                anio_lanzamiento = f"Anio Lanzamiento con mas horas jugadas para {genero}"
                genero_dicc[anio_lanzamiento] = int(anio_max)
            
                return genero_dicc
            else:
                return f"La palabra {genero} no se encuentra en la base de datos"
        else:
            return "Ingrese un valor valido: String"
    except NameError:
        return "Ingrese un valor valido: String"
    
#Segunda Funcion-----------------------------------------------------------

@app.get("/UserForGenre/{genero}", name = "Usuarios Por Genero")
#def UserForGenre( genero : str ) 
#return: **Ejemplo de retorno: {"Usuario con más horas jugadas para genero" : us213ndjss09sdf, 
#"Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}**.
def UserForGenre(genero : str):
    try:
        if type(genero) == str:

            genero = genero.lower().title()
            usergenre_data = pd.read_parquet("Henry-Assesment\\data\\usergenre_data")
            lista_genero = usergenre_data["genres"].unique()

            if genero in lista_genero:

                data_genero = usergenre_data[usergenre_data["genres"] == genero]
                usuario_max = data_genero.groupby("user_id")["playtime_forever"].sum().idxmax()
                max_by_year = data_genero[data_genero["user_id"] == usuario_max].groupby("release_year")["playtime_forever"].sum()
                df_max_by_year = pd.DataFrame(max_by_year).reset_index()

                lista_aux = []

                for i in range(len(max_by_year)):

                    dicc_aux = {}
                    year = df_max_by_year["release_year"][i]
                    hour = df_max_by_year["playtime_forever"][i]
                    dicc_aux[year]=  hour
                    lista_aux.append(dicc_aux)
            
                return {"Usuario con mas horas jugadas para genero":usuario_max,
                    "Horas jugadas": lista_aux}
            else:
                return print(f"La palabra {genero} no se encuentra en la base de datos")
        else:
            return print("Ingrese un valor valido: String")
    except NameError:
        return print("Ingrese un valor valido: String")

#Tercera Funcion-----------------------------------------------------------

@app.get("/UsersRecommend/{anio}", name = "Recomendacion De Usuarios")
#* def UsersRecommend( año : int ), 
# return **Ejemplo de retorno: [{"Puesto 1" : genero_1}, {"Puesto 2" : genero_2},{"Puesto 3" : genero_3}]**
def UsersRecommend(anio : int):
    try:
        if type(anio) == int:

            usersrecommend_data = pd.read_parquet("Henry-Assesment\\data\\usersrecommend_data")
            lista_anio = usersrecommend_data["release_year"].unique()

            if anio in lista_anio:
                
                data_bool = usersrecommend_data[usersrecommend_data["recommend"] == True]
                data_anio = data_bool[data_bool["release_year"] == anio]
                recommend_sum = data_anio.groupby("genres")["recommend"].sum()
                df_recommend_sum = pd.DataFrame(recommend_sum).sort_values("recommend",ascending=False).reset_index()
                
                list_aux = []

                for i in range(3):
                    dicc_aux = {}
                    dicc_aux[f"Puesto {i+1}"] = df_recommend_sum["genres"][i]
                    list_aux.append(dicc_aux)

                return list_aux

            else:
                return print(f"El anio {anio} no se encuentra en la base de datos")
        else:
            return print("Ingrese un valor valido: int")
    except NameError:
        return print("Ingrese un valor valido: int")

#Cuarta Funcion-----------------------------------------------------------

@app.get("/UsersNotRecommend/{int}", name = "No Recomendacion De Usuarios")
#* def UsersNotRecommend( año : int )
# return **Ejemplo de retorno: [{"Puesto 1" : genero_1}, {"Puesto 2" : genero_2},{"Puesto 3" : genero_3}]**
def UsersNotRecommend(anio : int):
    try:
        if type(anio) == int:

            usersrecommend_data = pd.read_parquet("Henry-Assesment\\data\\usersrecommend_data")
            lista_anio = usersrecommend_data["release_year"].unique()

            if anio in lista_anio:
                
                data_bool = usersrecommend_data[usersrecommend_data["recommend"] == False]
                data_anio = data_bool[data_bool["release_year"] == anio]
                recommend_sum = data_anio.groupby("genres")["recommend"].sum()
                df_recommend_sum = pd.DataFrame(recommend_sum).sort_values("recommend",ascending=False).reset_index()
                
                list_aux = []

                for i in range(3):
                    dicc_aux = {}
                    dicc_aux[f"Puesto {i+1}"] = df_recommend_sum["genres"][i]
                    list_aux.append(dicc_aux)

                return list_aux

            else:
                return print(f"El anio {anio} no se encuentra en la base de datos")
        else:
            return print("Ingrese un valor valido: int")
    except NameError:
        return print("Ingrese un valor valido: int")

#Quinta Funcion-----------------------------------------------------------

@app.get("/sentiment_analysis/{int}", name = "Analisis De Sentimientos")
#* def sentiment_analysis( año : int )
#  return **Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}**
def sentiment_analysis(anio : int):
    try:
        if type(anio) == int:

            sentiment_data = pd.read_parquet("Henry-Assesment\\data\\sentiment_data")
            lista_anio = sentiment_data["release_year"].unique()

            if anio in lista_anio:
                
                sentiment_data = pd.read_parquet("Henry-Assesment\\data\\sentiment_data").dropna()
                lista_anio = sentiment_data["release_year"].unique()
                data_anio = sentiment_data[sentiment_data["release_year"] == anio].drop(columns="item_id")
                df_data_anio = pd.DataFrame(data_anio.value_counts()).sort_index()

                list_aux = []
                list_sentiment=["Negative","Neutral","Positve"]


                for i, sentimiento in enumerate(list_sentiment):
                    dicc_aux = {}
                    dicc_aux[sentimiento] = int(df_data_anio.iloc[i])
                    list_aux.append(dicc_aux)

                list_aux

                return list_aux

            else:
                return print(f"El anio {anio} no se encuentra en la base de datos")
        else:
            return print("Ingrese un valor valido: int")
    except NameError:
        return print("Ingrese un valor valido: int")
    
    
    #Machine Learning Funcion-----------------------------------------------------------

@app.get("/recomendacion_juego/{str}", name = "Recomendacion de juegos")
def recomendacion_juego(id_producto):
    # Obtencion del Dataset

    item_data = pd.read_parquet("Henry-Assesment\\data\\steam_game_data")
    col_drop = ["release_date", "tags", "specs", "price", "early_access", "developer", "release_year"]
    item_data.drop(columns= col_drop, inplace=True )

    #Reducimos el tamanio de la data a un 20% del total debido a la incapacidad de procesar tanta informacion

    item_data = item_data.sample(frac=1/5, random_state=42).reset_index()

    # Usamos procesamiento de texto para generar una matriz TF-IDF

    tfidf = TfidfVectorizer(stop_words="english")
    item_data["genres"] = item_data["genres"].fillna("")
    tfidf_matrix = tfidf.fit_transform(item_data["genres"])  # Vector TF-IDF

    # Entrenamiento similitud del coseno

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    idx = item_data[item_data["id"] == id_producto].index[0]  # Encuentra el indice del juego
    sim_scores = list(enumerate(cosine_sim[idx]))  # Lista de puntuacion similitud en relacion al indice
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Organizo los indices de mayor a menor
    sim_scores = sim_scores[1:6]  # Top 5 juegos recomendados (sin tomar el idx 0 ya que es el mismo juego)
    game_indices = [i[0] for i in sim_scores]  # Tomo la primera posicion de las duplas formadas por sim_scores

    print(f"Juego Seleccionado:  {item_data[item_data['id'] == id_producto].iloc[0]}")

    return item_data[["genres","title","id"]].iloc[game_indices]
